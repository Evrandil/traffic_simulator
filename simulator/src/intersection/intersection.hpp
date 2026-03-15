#pragma once

#include<cstdio>



enum light_state	{
	RED,
	GREEN,
};

class intersection	{
	public:
		light_state lights_state;
		intersection();
		~intersection();
		void ToggleLights();
		light_state	GetLightsState();
		void	SetLightsState(light_state value);
};
