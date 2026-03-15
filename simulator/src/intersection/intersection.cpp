#include"intersection.hpp"



intersection::intersection()	{
	printf("Intersection created!\n");
	green_lights_state = green_light_state::UP_AND_DOWN;
}
intersection::~intersection()	{
	printf("Intersection deleted!\n");
}
green_light_state	intersection::GetGreenLightsState()	{
	return green_lights_state;
}
void	intersection::SetGreenLightsState(green_light_state value)	{
	green_lights_state = value;
}
void	intersection::ToggleLights()	{
	switch	(green_lights_state)	{
		case green_light_state::UP_AND_DOWN:
			green_lights_state = green_light_state::LEFT_AND_RIGHT;
			break;
		case green_light_state::LEFT_AND_RIGHT:
			green_lights_state = green_light_state::UP_AND_DOWN;
			break;
	}
}
