//
// Created by krawus on 5/31/22.

#include "../include/robot40_motion_planner/motion_planner_UR.hpp"
#include "motion_planner_UR.cpp"


int main(int argc, char **argv) {
    std::cout << "workin'...\n";
    ros::init(argc, argv, "right_arm");
    ros::AsyncSpinner spinner(1);
    spinner.start();

    //wczytanie struktury robota
    robot_model_loader::RobotModelLoader robot_model_loader("robot_description");
    robot_model::RobotModelPtr kinematic_model = robot_model_loader.getModel();
    planning_scene::PlanningScene planning_scene(kinematic_model);


    collision_detection::CollisionRequest collision_request;
    collision_detection::CollisionResult collision_result;
    std::vector<double> joint_config;
    bool inCollision;


    //10 x resetowanie wyniku kolizji, losowanie konfiguracji w przegubach i sprawdzanie czy jest kolizja
    for (int i = 0; i < 10; i++) {
        collision_result.clear();
        robot_state::RobotState &current_state = planning_scene.getCurrentStateNonConst();
        current_state.setToRandomPositions();
        const robot_model::JointModelGroup* joint_model_group =
                current_state.getJointModelGroup("right_arm");
        current_state.copyJointGroupPositions(joint_model_group, joint_config);
        planning_scene.checkSelfCollision(collision_request, collision_result);
        ROS_INFO_STREAM("Current state is "
                                << (collision_result.collision ? "in" : "not in")
                                << " self collision");

        if(collision_result.collision)
            inCollision=1;
        else
            inCollision=0;
    }



    return 0;
}
