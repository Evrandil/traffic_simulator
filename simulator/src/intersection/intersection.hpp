#pragma once

#include<cstdio>



enum green_light_state	{
	UP_AND_DOWN,
	LEFT_AND_RIGHT,
};

class intersection	{
	green_light_state green_lights_state;
	public:
		intersection();
		~intersection();
		void ToggleLights();
		green_light_state	GetGreenLightsState();
		void	SetGreenLightsState(green_light_state value);
};
