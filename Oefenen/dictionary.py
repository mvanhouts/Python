buildings = {"Burj Khalifa": (1,"Dubai", "UAE", 828),
    "Shanghai Tower": (2,"Shanghai", "China", 632),
    "Abraj Al-Bait Clock Tower": (3,"Mecca", "Saudi Arabia", 601),
    "Ping An Finance Center": (4,"Shenzhen", "China", 599),
    "Lotte World Tower": (5,"Seoul", "South Korea", 554),
    "One World Trade Center": (6,"New York City", "USA", 541)
    }


for buildingName, buildingDetails in buildings.items():
    print("{0} in {1} is {2} metres high".format(buildingName,buildingDetails[1],buildingDetails[3]))
