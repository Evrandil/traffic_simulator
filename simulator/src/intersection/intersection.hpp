#pragma once

#include<cstdio>



enum light_state	{
	RED,
	GREEN,
};

class intersection	{
	light_state lights_state;
	public:
		intersection();
		~intersection();
		void ToggleLights();
		light_state	GetLightsState();
		void	SetLightsState(light_state value);
};
