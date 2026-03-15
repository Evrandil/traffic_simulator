#include"lane/lane.hpp"
#include"intersection/intersection.hpp"



int main()	{
	lane *pas = new lane;
	car *some_car = new car;
	pas->AddVehicle(some_car);
	vehicle *and_another_one = new vehicle;
	pas->AddVehicle(and_another_one);
	pas->RemoveVehicle();
	delete pas;

	intersection *intersect = new intersection;
	printf("%d\n", intersect->GetGreenLightsState());
	intersect->ToggleLights();
	printf("%d\n", intersect->GetGreenLightsState());
	intersect->SetGreenLightsState(green_light_state::UP_AND_DOWN);
	printf("%d\n", intersect->GetGreenLightsState());
	delete intersect;
	return 0;
}
