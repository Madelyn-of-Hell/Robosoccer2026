# Robosoccer2026

##### Research
- PCB design/building
- Colour/light sensors
- Bluetooth  chip %% NOTE: ESPs can come with this built in %% 
- Camera
	- Could Stick with the OpenMV Cameras
		- Pro: We already have them
		- Pro: Others seem to use them a lot so we could find example code
		- Pro: I have the RPC code to connect them to arduino & like systems
		- Con: Need to detach breakout board
		- Con: Ours may be slightly non-functional so we'd need to figure that out earlyy
- Initial State config
	- Could do myriad individual switches for each config option
		- NOTE: Appears to be the standard at nationals
		- Pro: Enables greater clarity, 
		- Pro: Stateless; can be checked at any time
		- Con: Would use a lot of pins
		- Con: Could handle at most a ternary option (0,1,Off)
	- Could use a rotary dial system (like how old vaults do, keep switching direction in order to indicate moving on to the next thing)
		- Pro: Requires only one part (decreased port usage)
		- Pro: Allows for significantly greater options (dials i've looked at have up to 8 and i'm sure we could find more)
		- Con: Requires knowledge of a more complex system (could be alleviated by making a PDF, but would still introduce potential for error; should likely have a single designated driver to reduce possibility of false encoding)
- Microcontroller
	- FARLEY'S RECOMMENDATION: **ESP32** MICROCONTROLLER
	- Teensy 4.1
		- Language: C++
	- Arduino
		- (C++ via the arduino IDE) (my preference because guaranteed functionality with cameras)
	- RasPi
- Motors
	- Servo type? (brushless / stepper?) DC appropriate?
	- Needs decent torque so we're not pushed around by competitors
- Omni wheels
	- Bigger means we need less fast motors
	- ASK PATANE
- Gyroscope (compass; we just need yaw) (Included in the Sparkfun OTOS)
- Position sensor???? (Optical Tracking Odomotry Sensor)
	- Pro: Gives us precise and accurate positioning of both robots, enabling cool trig shit
	- Con: Requires hardcoded starting positions (config on startup)
	- Pro: Could teach robots to chart courses and relay them to one another so they don't collide.
		- Con?: Requires a comprehensive system for determining enemy positions and trajectories, as well as the framework for creating routes and determining whether the robot can make 
- Dribbler?
	- Consider hiding the ball behind the robot (like in open, but not really done in lightweight)
		- Pro: Requires complex, **fast** rotation and planning
	- Con: Requires absolute, real human units of measurement for distance, with (preferably) centimetre precision
- Carapace
	- Mainly 3D printed
	- Padded base to prevent damage?
	- Electronic components should have dedicated wells to avoid getting knocked out of place in case of collision
	- Need to determine filament types
		- Spongy, springy filament for shell and a more rigid material for the interior?
		- Clear filament for mirror tube
	- Requirements:
		- Should be maximum feasible size
		- Should have wheel positions denoted (needs wells for our motors)
		- Should have dedicated place for light sensor PCB in base
		- Should have dedicated position for OTOS in base
		- Should have dedicated dribbler well
		- Should have  dedicated camera well (needs to house the openmv camera and suspend the 100mm ball an arbitrary distance away.)
		- Should have dedicated well for rotary encoder (doesn't need to be precise for now, just a general alotted place to put it in the structure)
		- Should have dedicated well for batteries (doesn't need to be precise for now, just a general alotted place to put it in the structure)
		- Should have dedicated well for speed controller (doesn't need to be precise for now, just a general alotted place to put it in the structure)
		- Should have capacity to attach a steel plate for added weight customisation
	- Steel plate for weight customisation
##### Points to note from other competitors
- If robots are relying on communication, make them check if the other is still present every so often and have a plan for if it's not (e.g. switch to attack mode)
	- Maybe have a custom "stalling" mode? (get hold of the ball and just stay away from the other players)
##### Admin
- Ask Team Legacy about Dynasty homage



motor drivers
power logic & motors separately to avoid spikes