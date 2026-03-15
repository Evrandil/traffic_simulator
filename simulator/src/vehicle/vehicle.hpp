#pragma once



class vehicle	{
	public:
	vehicle* next;
		vehicle()	{	next = nullptr;	printf("Vehicle created!\n");	}
		~vehicle()	{	printf("Vehicle deleted!\n");	}
};

#include"car/car.hpp"
