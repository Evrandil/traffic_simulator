#include"lane.hpp"



lane::lane()	{
	head = nullptr;
	tail = nullptr;
	size = 0;
	printf("Lane created!\n");
}
lane::~lane()	{
	printf("Deleting line, amount of cars to delete:\t%d\n", size);
	if	(0 == size)	goto lane_finish;
	while	(1 != size)	{
		vehicle *nextHead = head->next;
		delete head;
		head = nextHead;
		--size;
	}
	delete head;
	--size;
	head = nullptr;
	tail = nullptr;
lane_finish:
	printf("Lane deleted\n");
}
/*
void	lane::AddVehicle(vehicle &newVehicle)	{
	if	(0 == size)	{
		head = &newVehicle;
	}	else	{
		tail->next = &newVehicle;
	}
	tail = &newVehicle;
	size++;
	printf("Vehicle added!\n");
}
*/
void	lane::AddVehicle(vehicle *newVehicle)	{
	if	(0 == size)	{
		head = newVehicle;
	}	else	{
		tail->next = newVehicle;
	}
	tail = newVehicle;
	size++;
	printf("Vehicle added!\n");
}
void	lane::RemoveVehicle()	{
	if	(0 == size)	throw(std::out_of_range("Cannot delete vehicle from empty lane!\n"));
	head = head->next;
	if	(1 == size)	tail = nullptr;
	--size;
	printf("Vehicle removed!\n");
}
