init python:

    class Building(object):
        '''Base class for castle buildings'''
        def __init__(self, uid):
            self.uid = uid
            self.name = "I should not exist"
            self.available = False
            self.lvl = 0
            self.max_lvl = 0
            self.costs = []
            self.income = 0
            self.incomes = []
            self.maintenance = 0
            self.maintenances = []
            self.morale = 0
            self.morales = []
            self.research = 0
            self.researches = []
            self.capacity = 0
            self.capacities = []
            self.recruitment = 0
            self.recruitments = []
            self.thumbnail = None
            self.prereqs = []
            self.perks = []
            self.description = "Prototype class for Building, you should not see this"

        @property
        def up_cost(self):
            '''Returns the price of new building or next upgrade'''
            if self.lvl < len(self.costs):
                return self.costs[self.lvl]
            else:
                return 0

        def build(self):
            '''Builds new upgrade level for the building'''
            if self.lvl >= self.max_lvl:
                return
                
            self.income = self.incomes[self.lvl]
            self.maintenance = self.maintenances[self.lvl]
            self.morale = self.morales[self.lvl]
            self.research = self.researches[self.lvl]
            self.capacity = self.capacities[self.lvl]
            self.recruitment = self.recruitments[self.lvl]

            self.lvl += 1

        def weekly(self):
            '''Called each week to update state'''
            pass

        def can_be_built(self):
            '''Returns True if all conditions for upgrading to next level are met'''
            # can be built if there is enough money and if an upgrade is not already scheduled and if current level is less than max level
            if self.lvl < self.max_lvl:
                if len(castle.scheduled_upgrades) == 0:
                    if self.costs[self.lvl] <= castle.treasury:
                        return True
            return False
                

        def can_be_shown(self):
            '''Returns True if building can be shown to player'''
            if self.lvl > 0:
                return True
            else:
                return False

    class Barracks(Building):
        '''Generic barracks but really just an orc den until maybe some gobbo troops get into the game and maybe Breeding Pit becomes a subclass because of driders'''
        def __init__(self, uid):
            super(Barracks, self).__init__(uid)
            self.name = "Orc Barracks"
            self.available = True
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_Barracks.png'
            self.prereqs = [["Already Built"],
                            ["Requires Technology: Ordering Chaos"],
                            ["Requires Technology: Military Logistics"],
                            ]
            self.perks = [["Orc soldier capacity 30", "Orc recruitment 1"],
                          ["Orc solder capacity 30->50", "Orc recruitment 1->3"],
                          ["Orc solder capacity 50->70", "Orc recruitment 3->5"]
                          ]
            self.description = "A facility for housing and training orc soldiers.  Every week, any new soldiers that Andras has recruited and trained will be brought here and added to the total available soldiers. They will also be armed and armored with any available equipment from a forge, should we have one.\
Expansions and upgrades to the barracks with increase the amount of soldiers that can be kept on hand for any missions or conquests they are needed for. However, the more soldiers we have at once the more we will have to pay and the more difficult it will be to keep morale up. Other infrastructure will be needed to handle the needs of the soldiers. On the other hand, who doesn't love hot sweaty greenskins."
            self._troops = 0
            self.equipment = 0
            self.troop_type = 'orc'
            self.costs = [100, 200, 300]
            self.incomes = [0, 0, 0]
            self.capacities = [30, 50, 70]
            self.morales = [0, 0, 0]
            self.researches = [0, 0, 0]
            self.maintenances = [0, 0, 0]
            self.recruitments = [1, 3, 5]
            self.lvl = 0
            self.max_lvl = 1
            self.build()

        def weekly(self):
            self.troops += self.recruitment + castle.recruitment_bonuses.get(self.uid, 0)
            if self.troops >= self.capacity:
                self.troops = self.capacity

        @property
        def troops(self):
            return self._troops

        @troops.setter
        def troops(self, val):
            self._troops = min(val, self.capacity)
            self._troops = max(self._troops, 0)

    class DarkSanctum(Barracks):
        '''A place where the troops need to be seperated with a fire hose'''        
        def __init__(self, uid):
            super(DarkSanctum, self).__init__(uid)
            self.name = "Dark sanctum"
            self.available = True
            # remove equipment (cubis don't use it)
            del self.equipment
            self.costs = [150, 300]
            self.incomes = [0, 0]
            self.maintenances = [4, 8]
            self.morales = [0.2, 0.2]
            self.researches = [0, 0]
            self.capacities = [5, 10]
            self.recruitments = [1, 1]
            self.troop_type = 'cubi'
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_Sanctum.png'
            self.prereqs = [["No prerequisites for Level 1"],
                            ["Requires technology: Dark Subterfuge"],
                            ]
            self.perks = [["Incubus and Succubus capacity 5", "Weekly recruitment rate 1","Weekly morale +0.2","Weekly research +0.5 rp", "Weekly maintainence 4"],
                          ["Incubus and Succubus capacity 5->10", "Weekly recruitment rate 1","Weekly morale +0.2->0.4","Weekly research +0.5->1.0 rp", "Weekly maintainence 4->8"],
                         ]
            self.description = "A proper army needs more than just soldiers.  The Dark Sanctum is the first step in adding magic users to the twin's forces.  It can accommodate a cadre of incubus and succubus sorcerers that will support the regular armies in times of war, as well as assist in research during times of peace.  In addition to providing their own military strength, each cubi will also add a small multiplier to the overall combat strength of all soldiers in the castle.  They also have the added bonus of helping to keep up morale, given the habit of cubi taking casual lovers from the ranks of troops.  Research and upgrades will allow more magical facilities to be constructed and increase the number of cubis that can be accommodated.\
Once the sanctum is completed, prisoners will be able to be turned over to the cubi to motivate them and inspire breakthroughs in research.  Each prisoner offered will produce an immediate one time research point boost.  Rowan may see where Cubi are coming from when he sets up the Dark Sanctum."
            self.lvl = 0
            self.max_lvl = 1

        def weekly(self):
            if self.lvl == 0:
                return

            castle.morale += self.morale
            castle.treasury -= self.maintenance

            self.troops += self.recruitment + castle.recruitment_bonuses.get(self.uid, 0)
            if self.troops >= self.capacity:
                self.troops = self.capacity

    class Forge(Building):
        '''Converts some iron to equipment'''
        def __init__(self, uid):
            super(Forge, self).__init__(uid)
            self.name = "Forge"
            self.available = True
            self.costs = [150, 600]
            self.incomes = [30, 60]
            self.maintenances = [10, 15]
            self.researches = [0, 0]
            self.capacities = [3, 6]
            self.morales = [0, 0]
            self.recruitments = [0, 0]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_Forge.png'
            self.prereqs = [["Immediately available at Level 1"],
                            ["Requires Technology: Smelting"],
                           ]
            self.perks = [["Weekly maintenance cost 10", "Weekly iron production capacity 3"],
                          ["Weekly maintenance cost 10->15", "Weekly iron production capacity 3->6"],
                         ]
            self.description = "A place where the smiths turn raw ore into works of art, destruction, and protection.  The forge is used to convert materials like iron into useable equipment for your soldiers.  An orc armed with proper metal equipment has nearly twice the military capacity as an unequipped one.  Even if there are no soldiers in need of equipment, gear produced by the forge will sell for much more than raw ore.  Research and upgrades can improve the quality and quantity of equipment produced, as well as eventually learning how to produce magical arms and armor.  Excess iron sells for 1 per unit.  Excess equipment sells for 5 per outfit. Rowan's lifestyle becomes more bullish with a Forge installed"
            self.lvl = 0
            self.max_lvl = 1

        def weekly(self):
            if hasattr(all_actors["alexia"], "job_state") and all_actors["alexia"].job_state.job == "forge" and castle._iron >= self.capacity + 2:
                castle._iron -= self.capacity
                castle._equipment += self.capacity
                
            elif castle._iron >= self.capacity:
                castle._iron -= self.capacity
                castle._equipment += self.capacity

            else:
                castle._equipment += castle._iron
                castle._iron = 0

    class Dungeon(Building):
        '''Dungeon (contains prisoners)'''
        def __init__(self, uid):
            super(Dungeon, self).__init__(uid)
            self.name = "Dungeon"
            self.available = True
            self._prisoners = 0
            self.costs = [0]
            self.capacities = [10]
            self.maintenances = [0]
            self.incomes = [0]
            self.morales = [0]
            self.researches = [0]
            self.recruitments = [0]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_CastleDungeon.png'
            self.prereqs = [["Already built and not expandable"]]
            self.perks = [["Capacity for 10 prisoners"]]
            self.description = "A section of the underground dedicated to holding prisoners. These are generally acquired after towns or fortresses have been sacked and can later be, employed, in other roles based on what structures we have completed in the castle. However, selling slaves will always be available should some quick money be needed.\
Upgrades here will increase the amount of prisoners that can be kept at once, but there is no such option at the moment"
            
            # init prisoners status
            # records current status of operations with prisoners (current, week limit)
            self.prisoners_status = {
                'slave': [0, 10],
                'ransom': [0, 3],
                'gladiator': [0, 3],
                'test': [0, 5]}
            # state of "auto-sell" for prisoners
            self.prisoners_auto = {
                'slave': False,
                'ransom': False,
                'gladiator': False,
                'test': False}
            self.lvl = 0
            self.max_lvl = 1
            self.build()

        def weekly(self):
            # auto sell prisoners
            while self.prisoners > 0:
                if castle.morale < 20 and (self.prisoners_status['gladiator'][0] < self.prisoners_status['gladiator'][1]) and self.prisoners_auto['gladiator']:
                    castle.morale += 3
                    self.prisoners -= 1
                    self.prisoners_status['gladiator'][0] += 1
                elif (self.prisoners_status['ransom'][0] < self.prisoners_status['ransom'][1]) and self.prisoners_auto['ransom']:
                    castle.treasury += 10
                    self.prisoners -= 1
                    self.prisoners_status['ransom'][0] += 1
                elif castle.morale >= 20 and castle.morale < 60 and (self.prisoners_status['gladiator'][0] < self.prisoners_status['gladiator'][1]) and self.prisoners_auto['gladiator']:
                    castle.morale += 3
                    self.prisoners -= 1
                    self.prisoners_status['gladiator'][0] += 1
                elif (self.prisoners_status['test'][0] < self.prisoners_status['test'][1]) and self.prisoners_auto['test']:
                    castle.rp += 2
                    self.prisoners -= 1
                    self.prisoners_status['test'][0] += 1
                elif (self.prisoners_status['slave'][0] < self.prisoners_status['slave'][1]) and self.prisoners_auto['slave']:
                    castle.treasury += 5
                    self.prisoners -= 1
                    self.prisoners_status['slave'][0] += 1
                elif (self.prisoners_status['gladiator'][0] < self.prisoners_status['gladiator'][1]) and self.prisoners_auto['gladiator']:
                    castle.morale += 3
                    self.prisoners -= 1
                    self.prisoners_status['gladiator'][0] += 1
                else:
                    # if there is no valid option for auto sell, end auto selling
                    break
            # reset current status for prisoners limits
            self.prisoners_status['slave'][0] = 0
            self.prisoners_status['ransom'][0] = 0
            self.prisoners_status['gladiator'][0] = 0
            self.prisoners_status['test'][0] = 0

        @property
        def prisoners(self):
            return self._prisoners

        @prisoners.setter
        def prisoners(self, val):
            self._prisoners = min(val, self.capacity)
            self._prisoners = max(self._prisoners, 0)
            
    class Brothel(Building):
        '''Brothel (contains spies)'''
        def __init__(self, uid):
            super(Brothel, self).__init__(uid)
            self.name = "Brothel"
            self.available = True
            self.costs = [200, 300]
            self.incomes = [0, 0]
            self.maintenances = [5, 6]
            self.morales = [0.5, 0.5]
            self.capacities = [2, 3]
            self.researches = [0.5, 0.5]
            self.recruitments = [0, 0]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_Brothel.png'
            self.prereqs = [["Requires Technology: Fiendish Diplomacy"],
                            ["Requires Technology: Silks and Smiles"],
                           ]
            self.perks = [["Weekly maintenance 5", "Spy capacity 2", "Weekly morale +0.5", "Weekly research 0.5 rp"],
                          ["Weekly maintenance 5->6", "Spy capacity 2->3", "Weekly morale +0.5->1.0", "Weekly research 0.5->0.75"],
                         ]
            self.description = "Ahh the oldest profession.... Except this thing is buried deep in a basement of a castle and not some building next to a Tavern. This is more a spy den, employee lounge and VIP room that Jezera can play around in.  You might want to leave a spy slot open for a certain incubus who likes corrupting nuns."
            self.spies = []
            self.available_spies = []
#
#  Not available for build at game start
#
            self.lvl = 0
            self.max_lvl = 0

            
        def weekly(self):
            # delete unrecruited spies
            for uid in self.available_spies:
                del_object(uid)
            self.available_spies = []
            # create new spies to recruit from
            for sex in ['m', 'f']:
                for i in range(self.lvl):
                    self.available_spies.append(Spy(sex).uid)

        def build(self):
            super(Brothel, self).build()
            self.weekly()
            print self.available_spies
            
    class BreedingPit(Building):
        '''Breeding pit (contains various monsters)'''
        def __init__(self, uid):
            super(BreedingPit, self).__init__(uid)
            self.name = "Breeding pit"
            self.available = True
            self.costs = [300]
            self.maintenances = [0]
            self.researches = [2]
            self.capacities = [12]
            self.incomes = [0]
            self.morales = [0]
            self.recruitments = [0]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_BreedingPit.png'
            self.prereqs = [["Requires Technology: Monster Taming"]]
            self.perks = [["Capacity for 12 driders but there are other oddballs"]]
            self.description = "This starts off as a nursery for hatching Drider eggs and training the hatchlings for work complete with all sorts of shenanigans during their mishandling.  Alexia may develop a taste for sushi after a few shifts.  We also can have both her and Rowan finding out about a newly introduced character's talent at wrangling trouser snakes."
            self._driders = 0
            self.drider_recruitment = 0
            self.lvl = 0
            self.max_lvl = 0

#        @property
#        def capacity(self):
#            return self._capacity + self.bonus_capacity
#
#        @capacity.setter
#        def capacity(self, val):
#            self._capacity = val - self.bonus_capacity
#
#        @property
#        def bonus_capacity(self):
#            for ac in all_actors.values():
#                if hasattr(ac, 'job_state'):
#                    if ac.job_state.job == 'breeding':
#                        return 8
#            return 0

        @property
        def maintenance_discount(self):
            for ac in all_actors.values():
                if hasattr(ac, 'job_state'):
                    if ac.job_state.job == 'breeding':
                        return int(10 * all_actors[ac.uid].job_state.efficiency())
            return 0

        @property
        def free_space(self):
            # free space = capacity - number_of_monsters1 * size1 - ...
            return self.capacity - self.monsters

        @property
        def driders(self):
            # return number of 'whole' driders
            return int(self._driders)

        @property
        def monsters(self):
            '''Returns total number of "whole" monsters, disregarding their size'''
            # TODO: multiply by size for large monsters
            return self.driders

        def weekly(self):
            if self._driders < self.capacity:
                if hasattr(all_actors["alexia"], "job_state") and all_actors["alexia"].job_state.job == "breeding":
                    self._driders += self.drider_recruitment + 0.5
                else:
                    self._driders += self.drider_recruitment

    class CastleHall(Building):
        '''Castle Hall as a proper class'''
        def __init__(self, uid):
            super(CastleHall, self).__init__(uid)
            self.name = "Castle Hall"
            self.available = True
            self.costs = [0, 400, 600]
            self.capacities = [0, 0, 0]
            self.maintenances = [25, 30, 40]
            self.incomes = [50, 70, 90]
            self.researches = [0, 0, 0]
            self.recruitments = [0, 0, 0]
            self.morales = [3, 3.5, 4]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_ThroneRoom.png'
            self.prereqs = [["Already built"],
                            ["Requires Technology: Fiendish Diplomacy"],
                            ["Requires Technology: Opulence"],
                           ]
            self.perks = [["Income 50", "Morale increase 3"],
                          ["Income 50->70", "Morale increase 3->3.5"],
                          ["Income 70->90", "Morale increase 3.5->4"],
                         ]
            self.description = "A more impressive court will make our subjects more willing to comply and places us in a better negotiating position.  Restoring the castle's grandeur will not be a simple or inexpensive task, but will certainly have an impact on on the impressionable and those with darkness in their hearts.  It will also allow Jezera to improve and upgrade the general infrastructure of the entire surface half of the castle."
            self.lvl = 0
            self.max_lvl = 1
            self.build()
 
    class Library(Building):
        '''Library as a proper class'''
        def __init__(self, uid):
            super(Library, self).__init__(uid)
            self.name = "Library"
            self.available = True
            self.costs = [0, 200, 400]
            self.capacities = [0, 0, 0]
            self.maintenances = [0, 10, 20]
            self.incomes = [0, 0, 0]
            self.researches = [10, 12.5, 15]
            self.recruitments = [0, 0, 0]
            self.morales = [0, 0, 0]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_Library.png'
            self.prereqs = [["Already built at level 1"],
                            ["Requires Technology: Contact Network"],
                            ["Requires Technology: Research Infrastructure"],
                           ]
            self.perks = [["Maintenance cost 0", "Weekly research 10 RP"],
                          ["Maintenance cost 0->10", "Weekly research 12.5"],
                          ["Maintenance cost 10->20", "Weekly research 15"],
                         ]
            self.description = "The Bloodmeen library is one of the most extensive and well stocked collections in the whole of the Six Realms.  Cliohna has taken possession of it and uses it for both her own personal projects and as the center of operations for the magic and research projects of the castle. Expanding on the collection of books available must be done by finding libraries and abbeys in the world.\
However, what can be done here is investing our treasury into expanded laboratory facilities, equipment, and training staff for the library. These will allow Cliohna to both handle more magical related infrastructure in the castle and expand the scope of her research on Bloodmeen's behalf."
            self.lvl = 0
            self.max_lvl = 1
            self.build()

    class Tavern(Building):
        '''Tavern as a proper class'''
        def __init__(self, uid):
            super(Tavern, self).__init__(uid)
            self.name = "Tavern"
            self.available = True
            self.costs = [150, 300]
            self.capacities = [0, 0]
            self.maintenances = [0, 0]
            self.incomes = [30, 60]
            self.researches = [0, 0]
            self.recruitments = [0, 0]
            self.morales = [0, 0]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_Tavern.png'
            self.prereqs = [["Immediately available to build at level 1"],
                            ["Requires technology: Fiendish Diplomacy", "Requires technology: Silks and Smiles"],
                           ]
            self.perks = [["Weekly income 30"],
                          ["Weekly income 30->60"]
                         ]
            self.description = "On the long road between the Empire of Sand and the great Forest of Ealoaen, lies the ruins of what was once a sanctuary in the bleak Rakshan Wastes.  This tavern could be restored and used as a means of generating wealth to support the reconstruction of Castle Bloodmeen.  A portal site lies nearby, making it an ideal location to build and allowing staff to easily move between the two.  As the tavern grows and more traders take the overland route again, rumors and whispers will flow from these wooden walls.  The tavern will also serve as the perfect place to establish mercenary contracts.\
Building the tavern will allow you to trade with villages instead of occupying or destroying them.  This will pull in a small amount of income without needing to spend military forces on defeating the local defenders.  However, it will prevent you from removing the village's military capacity from its realm.\
Once the tavern is finished, it will be possible to find family members, business partners, or charitable sorts that are willing to ransom our prisoners for a larger amount of money than we'd get for simply selling them as slaves.  This is a slow process, and we will only be able to ransom a few prisoners each week."
            self.lvl = 0
            self.max_lvl = 1

    class Quarters(Building):
        '''Quarters as a proper class.  Shows as having two levels but lvl 2 not in game at the moment'''
        def __init__(self, uid):
            super(Quarters, self).__init__(uid)
            self.name = "Living Quarters"
            self.available = False
            self.costs = [0]
            self.capacities = [0]
            self.maintenances = [5]
            self.incomes = [0]
            self.researches = [0]
            self.recruitments = [0]
            self.morales = [0]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_LivingQuarters.png'
            self.prereqs = [["Already built"]]
            self.perks = [["Place to bang people in bed"]]
            self.description = "You will not see this since available is False."
            self.lvl = 0
            self.max_lvl = 1
            self.build()

    class Caravan(Building):
        '''Caravan as a proper class.  Looks like a wagon is a building when it's stalled.  Second tier not currently in the game'''
        def __init__(self, uid):
            super(Caravan, self).__init__(uid)
            self.name = "Caravan"
            self.available = False
            self.costs = [0, 300]
            self.capacities = [0, 0]
            self.maintenances = [0, 0]
            self.incomes = [0, 0]
            self.researches = [0, 0]
            self.recruitments = [0, 0]
            self.morales = [0, 0]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_Wagon.png'
            self.prereqs = [["Already built"]]
            self.perks = [["Maybe a store again one day"]]
            self.description = "No see um since available is False.  Maybe one day the devs will resurrect the store gui"
            self.lvl = 0
            self.max_lvl = 1
            self.build()


    class Kennel(Building):
        '''Kennel as a proper class.  Not in the game yet'''
        def __init__(self, uid):
            super(Kennel, self).__init__(uid)
            self.name = "Warg Kennel"
            self.available = False
            self.costs = [250]
            self.capacities = [0]
            self.maintenances = [0]
            self.incomes = [0]
            self.researches = [0]
            self.recruitments = [0]
            self.morales = [0]
            self.thumbnail = None
            self.prereqs = [["Requires Technology: Monster Taming"]]
            self.perks = [["Not worth building yet"]]
            self.description = "Not implemented yet so will not show on build gui"
            self.lvl = 0
            self.max_lvl = 0

    class Arena(Building):
        '''Arena as a proper class'''
        def __init__(self, uid):
            super(Arena, self).__init__(uid)
            self.name = "Arena"
            self.available = True
            self.costs = [200, 400]
            self.capacities = [0, 0]
            self.maintenances = [20, 30]
            self.incomes = [0, 0]
            self.researches = [0, 0]
            self.recruitments = [0, 0]
            self.morales = [2, 3]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_Arena.png'
            self.prereqs = [["Requires Technology: Ordering Chaos"],
                            ["Requires Technology: Military Logistics"],
                            ]
            self.perks = [["Weekly maintenance 20", "Weekly morale boost 2"],
                          ["Weekly maintenance 20->30", "Weekly morale boost 2->3"],
                          ]
            self.description =  "As the armies of the twins grow larger, they also grow more restless.  A fighting arena will provide the perfect place to blow off steam and keep spirits up.  However, this expensive facility will not provide many other benefits and should only be considered for construction if morale becomes a problem.  Upgrades will increase the capacity for entertainment.\
Once the arena is completed, prisoners may be used as gladiators and fodder for the soldiers.  They won't last long, but will give a significant boost to morale during their last days.\ Complimentary ball washer in VIP section."

            self.lvl = 0
            self.max_lvl = 0
            
    class Summoning(Building):
        '''Summoning as a proper class'''
        def __init__(self, uid):
            super(Summoning, self).__init__(uid)
            self.name = "Summoning Chambers"
            self.available = False
            self.costs = [300, 600]
            self.capacities = [0, 0]
            self.maintenances = [10, 10]
            self.incomes = [0, 0]
            self.researches = [1, 2]
            self.recruitments = [0, 0]
            self.morales = [0, 0]
            self.thumbnail = None
            self.prereqs = [["Requires Technology: Basic Summoning"]]
            self.perks = [["Nothing yet"]]
            self.description = "Not in the game again.  Maybe one day the devs will use this place as something other than an event spawner debug"
            self.lvl = 0
            self.max_lvl = 0

    class Workshop(Building):
        '''Workshop as a proper class'''
        def __init__(self, uid):
            super(Workshop, self).__init__(uid)
            self.name = "Workshop"
            self.available = False
            self.costs = [0]
            self.capacities = [0]
            self.maintenances = [0]
            self.incomes = [0]
            self.researches = [0]
            self.recruitments = [0]
            self.morales = [0]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_Workshop.png'
            self.prereqs = [["Aleady built and not upgradable"]]
            self.perks = [["You're looking at it"]]
            self.description = "This room, which serves as my planning and drafting room for all construction projects as well as ongoing excavations of the castle tunnels. This space is also where I tend to my hobbies and keep my tools.  Most of the actual work for any building projects will take place on-site, so upgrades and improvements to this building will be unnecessary.  Place for Skordred to blow off steam and a few other things."
            self.lvl = 0
            self.max_lvl = 1
            self.build()

    class NasimChamber(Building):
        '''NasimChamber as a proper class'''
        def __init__(self, uid):
            super(NasimChamber, self).__init__(uid)
            self.name = "Nasim Chamber"
            self.available = False
            self.costs = [80]
            self.capacities = [0]
            self.maintenances = [0]
            self.incomes = [0]
            self.researches = [2]
            self.recruitments = [0]
            self.morales = [0]
            self.thumbnail = None
            self.prereqs = [["Meet Nasim for the first time"]]
            self.perks = [["Weekly research 2 rp", "Furthers Nasim's research into boobies"]]
            self.description = "Keep toes behind the line or else body parts may start to re-arrange"

            self.lvl = 0
            self.max_lvl = 0

    class MagicBuilding(Building):
        def __init__(self, uid):
            super(MagicBuilding, self).__init__(uid)


    all_buildings = {
        'hall': CastleHall,
        'library': Library,
        'barracks': Barracks,
        'dungeon': Dungeon,
        'sanctum': DarkSanctum,
        'tavern': Tavern,
        'forge': Forge,
        'quarters': Quarters,
        'caravan': Caravan,
        'workshop': Workshop,
        'kennel': Kennel,
        'pit': BreedingPit,
        'brothel': Brothel,
        'arena': Arena,
        'summoning': Summoning,
        'nasim_chamber': NasimChamber
        }
