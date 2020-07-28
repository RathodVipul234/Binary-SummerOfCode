class gramToAll:
    def __init__(self,w1,w2):
        self.w1 = w1
        self.w2 = w2
    
    def gm_to_kg(self):
        w = float(self.w1) * 0.001
        return str(w) + ' kg\n'
    
    def gm_to_mg(self):
        w = float(self.w1) * 1000
        return str(w) + ' mg\n'
    
    def gm_to_ug(self):
        w = float(self.w1) * 1000000
        return str(w) + ' ug\n'

class kilogramToAll:
    def __init__(self,w1,w2):
        self.w1 = w1
        self.w2 = w2
    
    def kg_to_gm(self):
        w = float(self.w1) * 1000
        return str(w) + ' gm\n'
    
    def kg_to_mg(self):
        w = float(self.w1) * 1000000
        return str(w) + ' mg\n'
    
    def kg_to_ug(self):
        w = float(self.w1) * 1000000000
        return str(w) + ' ug\n'

class miligramToAll:
    def __init__(self,w1,w2):
        self.w1 = w1
        self.w2 = w2
    
    def mg_to_kg(self):
        w = float(self.w1) * 0.000001
        return str(w) + ' kg\n'
    
    def mg_to_gm(self):
        w = float(self.w1) * 0.001
        return str(w) + ' gm\n'
    
    def mg_to_ug(self):
        w = float(self.w1) * 1000
        return str(w) + ' ug\n'

class microgramToAll:
    def __init__(self,w1,w2):
        self.w1 = w1
        self.w2 = w2
    
    def ug_to_kg(self):
        w = float(self.w1) * 0.000000001
        return str(w) + ' kg\n'
    
    def ug_to_gm(self):
        w = float(self.w1) * 0.000001
        return str(w) + ' gm\n'
    
    def ug_to_mg(self):
        w = float(self.w1) * 0.001
        return str(w) + ' mg\n'

print("---------------------Weight Conversion(kg,gm,mg,ug)--------------------")
while True:
    print('For Exit Press ->  ctrl + c')
    print('-'*70 +'\n')
    try:
        unit_li = ['kg','gm','mg','ug']
        weight1 = input('Enter weight with unit seprated with space: ').split()
        if int(weight1[0]) < 0:
            print('Weight should be +ve.')
            continue
        if weight1[1] not in unit_li:
            print('Weight unit should be in kg/gm/mg/ug only.\n')
            continue
        unit = input('Enter unit for conversion(kg/gm/mg/ug): ')
        if unit in unit_li:
            if weight1[1] == unit:
                print(f"{weight1[0]} {unit}\n")
            
            elif weight1[1] == 'gm':
                if unit == 'kg':
                    gta = gramToAll(weight1[0],unit)
                    print(gta.gm_to_kg())
                elif unit == 'mg':
                    gta = gramToAll(weight1[0],unit)
                    print(gta.gm_to_mg())
                elif unit == 'ug':
                    gta = gramToAll(weight1[0],unit)
                    print(gta.gm_to_ug())

            elif weight1[1] == 'kg':
                if unit == 'gm':
                    gta = kilogramToAll(weight1[0],unit)
                    print(gta.kg_to_gm())
                elif unit == 'mg':
                    gta = kilogramToAll(weight1[0],unit)
                    print(gta.kg_to_mg())
                elif unit == 'ug':
                    gta = kilogramToAll(weight1[0],unit)
                    print(gta.kg_to_ug())

            elif weight1[1] == 'mg':
                if unit == 'kg':
                    gta = miligramToAll(weight1[0],unit)
                    print(gta.mg_to_kg())
                elif unit == 'gm':
                    gta = miligramToAll(weight1[0],unit)
                    print(gta.mg_to_gm())
                elif unit == 'ug':
                    gta = miligramToAll(weight1[0],unit)
                    print(gta.mg_to_ug())
            
            elif weight1[1] == 'ug':
                if unit == 'kg':
                    gta = microgramToAll(weight1[0],unit)
                    print(gta.ug_to_kg())
                elif unit == 'gm':
                    gta = microgramToAll(weight1[0],unit)
                    print(gta.ug_to_gm())
                elif unit == 'mg':
                    gta = microgramToAll(weight1[0],unit)
                    print(gta.ug_to_mg())
        else:
            print('Enter Proper unit.')
            continue

    except ValueError:
        print('Please Enter valid unit/number.')

    # except IndexError:
        # print('Follow proper format..')

    except KeyboardInterrupt:
        break