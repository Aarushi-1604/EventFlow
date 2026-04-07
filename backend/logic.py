"""
Crowd simulation and management rules for EventFlow AI.
"""
from typing import Dict, List
import random
from datetime import datetime

class CrowdSimulator:
    """
    Handles crowd simulation logic across different event zones.
    """
    def __init__(self, zones: List[str]):
        self.zones = zones
        # Initialize base capacity for each zone
        self.zone_capacities = {zone: random.randint(500, 2000) for zone in zones}
        self.current_occupancy = {zone: 0 for zone in zones}

    def simulate_movement(self) -> Dict[str, dict]:
        """
        Simulates the movement of crowds between zones.
        Returns the current state of all zones.
        """
        state = {}
        for zone in self.zones:
            # Simulate random influx and outflux
            change = random.randint(-50, 50)
            new_occupancy = max(0, self.current_occupancy[zone] + change)
            
            # Simple rule: Cap at capacity + a random overflow
            max_cap = self.zone_capacities[zone]
            if new_occupancy > max_cap * 1.1:
                new_occupancy = int(max_cap * 1.1)

            self.current_occupancy[zone] = new_occupancy
            
            state[zone] = {
                "occupancy": new_occupancy,
                "capacity": max_cap,
                "status": self._evaluate_crowd_status(new_occupancy, max_cap)
            }
        
        return state

    def _evaluate_crowd_status(self, occupancy: int, capacity: int) -> str:
        """
        Evaluates the status based on occupancy percentage.
        """
        ratio = occupancy / capacity if capacity > 0 else 0
        if ratio >= 0.9:
            return "Critical"
        elif ratio >= 0.75:
            return "Warning"
        return "Normal"

    def get_crowd_decision(self, intent: str) -> dict:
        """
        Suggests the best time, wait time, and zones based on user intent.
        Simulates peak vs off-peak times based on current time.
        """
        current_hour = datetime.now().hour
        # Simulating peak hours: 12 PM - 2 PM, 6 PM - 8 PM
        is_peak = (12 <= current_hour <= 14) or (18 <= current_hour <= 20)
        
        # simulated base wait in minutes
        base_wait = 20 if is_peak else 5
        current_wait = base_wait + random.randint(0, 15)
        
        # identify zones to avoid (occupancy >= 75%)
        avoid_zones = []
        for zone in self.zones:
            cap = self.zone_capacities.get(zone, 1)
            occ = self.current_occupancy.get(zone, 0)
            if (occ / cap) >= 0.75:
                avoid_zones.append(zone)

        best_zone = None
        if intent.lower() == 'food':
            # suggest the least crowded zone overall
            best_zone = min(
                self.zones,
                key=lambda z: self.current_occupancy.get(z, 0) / self.zone_capacities.get(z, 1)
            )
            
        return {
            "current_wait": f"{current_wait} mins",
            "best_time_to_go": "3:00 PM" if is_peak else "Now",
            "best_zone": best_zone,
            "avoid_zones": avoid_zones
        }
