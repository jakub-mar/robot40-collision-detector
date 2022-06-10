#include "../include/robot40_motion_planner/motion_planner_UR.hpp"
#include <random>
#include "robot40_motion_planner/motion_planner_UR.hpp"
#include <fstream>


bool satisfy_bounds(std::vector<double> joints, double low, double top)
{
    if ( (joints[0] > low && joints[0] < top) && (joints[1] > low && joints[1] < top) &&
    (joints[2] > low && joints[2] < top) && (joints[3] > low && joints[3] < top) &&
    (joints[4] > low && joints[4] < top) && (joints[5] > low && joints[5] < top) )
        return true;
    else
        return false;
}


int main(int argc, char **argv) {

    ros::init(argc, argv, "right_arm");
    ros::AsyncSpinner spinner(1);
    spinner.start();

    std::ofstream data;
    data.open("data_.csv");
    data<<"joint1,joint2,joint3,joint4,joint5,joint5,isCollision\n";

    //wczytanie struktury robota
    robot_model_loader::RobotModelLoader robot_model_loader("robot_description");
    robot_model::RobotModelPtr kinematic_model = robot_model_loader.getModel();
    planning_scene::PlanningScene planning_scene(kinematic_model);

    collision_detection::CollisionRequest collision_request;
    collision_detection::CollisionResult collision_result;
    std::vector<double> joint_config;
    bool inCollision;

    double lower_bound = -1.5708;
    double upper_bound = 1.5708;
    std::uniform_real_distribution<double> distr(lower_bound, upper_bound);
    bool inBounds = 0;

        for (int i = 0; i<100 ; i++) {

            collision_result.clear();
            robot_state::RobotState &current_state = planning_scene.getCurrentStateNonConst();
            inBounds=0;
            while (!inBounds) {
                current_state.setToRandomPositions();
                const robot_model::JointModelGroup* joint_model_group =
                        current_state.getJointModelGroup("right_arm");

                    current_state.copyJointGroupPositions(joint_model_group, joint_config);

                    if (satisfy_bounds(joint_config, lower_bound, upper_bound))
                        inBounds=true;
                    
            }

            planning_scene.checkSelfCollision(collision_request, collision_result);
            if(collision_result.collision)
                inCollision=1;
            else
                inCollision=0;

            data<<joint_config[0]<<","<<joint_config[1]<< ","<<joint_config[2]<<","<<
                joint_config[3]<<","<<joint_config[4]<<","<<joint_config[5]<<","<<inCollision<<"\n";

        }

    data.close();

    return 0;
}
