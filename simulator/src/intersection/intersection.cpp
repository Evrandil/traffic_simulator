#include"intersection.hpp"



intersection::intersection()	{
	printf("Intersection created!\n");
	lights_state = light_state::RED;
}
intersection::~intersection()	{
	printf("Intersection deleted!\n");
}
light_state	intersection::GetLightsState()	{
	return lights_state;
}
void	intersection::SetLightsState(light_state value)	{
	lights_state = value;
}
void	intersection::ToggleLights()	{
	switch	(lights_state)	{
		case light_state::GREEN:
			lights_state = light_state::RED;
			break;
		case light_state::RED:
			lights_state = light_state::GREEN;
			break;
	}
}
