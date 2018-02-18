import database

def definePeriod():
    period = [None]*3
    print("\n==== Create Period ====")
    time = input('Time Parcial [ex: 10:01]: ')
    distance = input('Distance [ex: 1.200]: ')
    velocity = input('Velocity [ex: 5.5]: ')
    period[0] = time
    period[1] = distance
    period[2] = velocity
    return period

def createRun(date):
    run = []
    print("\n==== Create Run ====")
    time_total = input('Time Total [ex: 60:12]: ')
    distance = input('Distance: [ex: 4.500]: ')
    calories = int(input('Calories [ex: 223]: '))
    qtd_periods = int(input('Quantity periods [ex: 2]: '))
    run.append(time_total)
    run.append(distance)
    run.append(calories)
    run.append(qtd_periods)
    while(qtd_periods>0):
        run.append(definePeriod())
        qtd_periods-=1
    return run

def showMenu():
    print('\n ==== Main Menu ====')
    print('1 - Add run')
    print('2 - Show all races')
    db = database.Database()
    if db.getSizeLstRegisters()>0:
        print('3 - Show race no save')
        print('4 - Save')      
    print('9 - Exit')
    
def actMenu(opc):
    db = database.Database()
    if opc==1:
        date = input('Inform the date of run [ex:2017/30/12]: ')
        run = createRun(date)
        db.include(run)
        return None
    if opc==2:
        print('\n === Show All === \n')    
        db.showAll()
    if opc==3 and db.getSizeLstRegisters()>0:
        print("Vazio",db.getLstRegisters())

    if opc==4 and len(db.db.getSizeLstRegisters())>0:
        result=save(race)
        if result==True:
            race=[]
            print('Save with sucess')
        else:
            print('Not save')
    if opc==9:
        return False  
def main():
    while True:
        showMenu()
        try:
            opc = int(input('\nInform number of option:'))
            actMenu(opc)
        except ValueError:
            print('Incorrect option')
    
    
if __name__ == "__main__":
    main()

                
