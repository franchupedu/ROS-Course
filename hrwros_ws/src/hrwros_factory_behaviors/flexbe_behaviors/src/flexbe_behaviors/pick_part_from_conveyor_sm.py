#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from hrwros_factory_states.set_conveyor_power_state import SetConveyorPowerState
from hrwros_factory_states.compute_grasp_state import ComputeGraspState
from flexbe_manipulation_states.moveit_to_joints_dyn_state import MoveitToJointsDynState as flexbe_manipulation_states__MoveitToJointsDynState
from hrwros_factory_states.vacuum_gripper_control_state import VacuumGripperControlState
from hrwros_factory_states.detect_part_camera_state import DetectPartCameraState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Feb 20 2020
@author: Francisco Peduto
'''
class PickpartfromconveyorSM(Behavior):
	'''
	This is a behavior for the hrwros factory simulation that picks a part from the conveyor belt using Robot 1
	'''


	def __init__(self):
		super(PickpartfromconveyorSM, self).__init__()
		self.name = 'Pick part from conveyor'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]

		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		pick_group = 'robot1'
		home1 = [1.5535, -1.588, 0.069, 1.57, -1.519, 0]
		gripper1 = 'vacuum_gripper1_suction_cup'
		names1 = ['robot1_shoulder_pan_joint', 'robot1_shoulder_lift_joint', 'robot1_elbow_joint', 'robot1_wrist_1_joint', 'robot1_wrist_2_joint', 'robot1_wrist_3_joint']
		# x:1188 y:362, x:442 y:319
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.part_pose = []
		_state_machine.userdata.pick_configuration = home1
		_state_machine.userdata.joint_names = []
		_state_machine.userdata.home1 = home1
		_state_machine.userdata.conveyor_speed = 100

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]

		# [/MANUAL_CREATE]


		with _state_machine:
			# x:46 y:30
			OperatableStateMachine.add('Start conveyor',
										SetConveyorPowerState(stop=False),
										transitions={'succeeded': 'Detect part', 'failed': 'failed'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'speed': 'conveyor_speed'})

			# x:867 y:12
			OperatableStateMachine.add('Compute pick configuration',
										ComputeGraspState(group=pick_group, offset=0.0, joint_names=names1, tool_link=gripper1, rotation=3.1415),
										transitions={'continue': 'Move Robot 1 to pick', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'part_pose', 'joint_values': 'pick_configuration', 'joint_names': 'joint_names'})

			# x:1136 y:29
			OperatableStateMachine.add('Move Robot 1 to pick',
										flexbe_manipulation_states__MoveitToJointsDynState(move_group=pick_group, action_topic='/move_group'),
										transitions={'reached': 'Activate gripper', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'pick_configuration', 'joint_names': 'joint_names'})

			# x:1113 y:145
			OperatableStateMachine.add('Activate gripper',
										VacuumGripperControlState(enable=True, service_name='/gripper1/control'),
										transitions={'continue': 'Move Robot to Home configuration', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:791 y:319
			OperatableStateMachine.add('Move Robot to Home configuration',
										flexbe_manipulation_states__MoveitToJointsDynState(move_group=pick_group, action_topic='/move_group'),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'home1', 'joint_names': 'joint_names'})

			# x:348 y:26
			OperatableStateMachine.add('Detect part',
										DetectPartCameraState(ref_frame='robot1_base', camera_topic='/hrwros/logical_camera_1', camera_frame='logical_camera_1_frame'),
										transitions={'continue': 'Stop conveyor belt', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'part_pose'})

			# x:602 y:25
			OperatableStateMachine.add('Stop conveyor belt',
										SetConveyorPowerState(stop=True),
										transitions={'succeeded': 'Compute pick configuration', 'failed': 'failed'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'speed': 'conveyor_speed'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]

	# [/MANUAL_FUNC]
