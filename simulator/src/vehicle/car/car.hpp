#pragma once

#include"../vehicle.hpp"



class car : public vehicle	{
	public:
		car()	{	printf("Car created!\n");	}
		~car()	{	printf("Car deleted!\n");	}
};
