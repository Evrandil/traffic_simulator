#pragma once

#include<cstddef>
#include<cstdio>
#include<stdexcept>
#include"../vehicle/vehicle.hpp"



class lane 	{
	public:
		vehicle *head;
		vehicle *tail;
		size_t size;
		lane();
		~lane();
//		void AddVehicle(vehicle&);
		void AddVehicle(vehicle*);
		void RemoveVehicle();
};
