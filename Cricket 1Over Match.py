while True:

    import random

    print("\n\tWELCOME TO ONE OVER CRICKET MATCH")

    TEAMS=input("\nENTER YOUR TEAM NAME: ").upper()
    OPPONENT_TEAMS=input("\nENTER YOUR OPPONENT TEAM NAME: ").upper()

    print(f"\nMatch Fixed With {TEAMS} \ VS / {OPPONENT_TEAMS}")

    Options=["HEADS","TAILS"]

    Yours=input("\nCHOOSE THE TOSS= HEADS OR TAILS: ").upper()

    Toss = random.choice(Options)

    print("\nYou are Choosed: ",Yours)
    print("Coin Flip Side: ",Toss)

# -----------------------------FIRST BALL STARTS FROM-------------------------------------------------------------------------


    run_choice=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
    run=run_choice
    reball_run=random.choice((0,1,2,3,4,6))
    reball=reball_run
    Noball=1
    Wide=1
    Out=0

    Opp_Team_FirstBall_Run = 0


    if Yours == "HEADS" and Toss == "TAILS" or Yours == "TAILS" and Toss == "HEADS":
        
        print(f"\nToss Win By {OPPONENT_TEAMS} and Choose The Bat First")
        print("\nReady To Bowl")

# ********************************B(OPPONENT TEAM) BATTING********************************************************************
            
        first_ball=input("\nPress ( 'ENTER' ) To Deliver The First Ball: ")

        if run == "Wide":
                print("\nBall Is: ",run)
                print("Extra Run: ",Wide)

                Reball_I=input("\nPress ( 'ENTER' ) To Deliver The Reball: ")

                if Reball_I == "":
                    print("\nWide Reball Run: ",reball)
                    
                    Opp_Team_FirstBall_Run += Wide+reball


                    print("\nTotal 1st Ball Run Is: ",Opp_Team_FirstBall_Run)

        elif run == "No Ball":

                print("\nBall Is: ",run)
                print("Extra Run Is: ",Noball, "No Ball Attend By: ",reball)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run=random.choice((0,1,2,3,4,6))
                FreeHit=Free_Run

                No_Reball_I= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                if No_Reball_I == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit)

                    Opp_Team_FirstBall_Run += Noball+reball+FreeHit
                    print("\nTotal 1st Ball Run Is: ",Opp_Team_FirstBall_Run)
            
        elif run == "Out":
                Opp_Team_FirstBall_Run += Out
                print("\nYou Are: ",run)
                print("\n1st Ball Out Consider As: ",Out)

        elif first_ball == "":
                Opp_Team_FirstBall_Run += run
                print("\n1st Ball Run: ",run)
                
                
        else:
                print("\nEnter The Correct Number")

# -----------------------------SECOND BALL STARTS FROM-------------------------------------------------------------------------

        run_choice2=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
        run2=run_choice2

        reball_run2=random.choice((0,1,2,3,4,6))
        reball2=reball_run2

        Noball2=1
        Wide2=1
        Out2=0

        Opp_Team_SecondBall_Run = 0
            
        second_ball=input("\nPress ( 'ENTER' ) To Deliver The Second Ball: ")

        if run2 == "Wide":
                print("\nBall Is: ",run2)
                print("Extra Run: ",Wide2)

                Reball_II=input("\nPress ( 'ENTER' ) Deliver The Reball: ")

                if Reball_II == "":
                    print("\nWide Reball Run: ",reball2)
                    
                    Opp_Team_SecondBall_Run += Wide2+reball2
                    print("\nTotal 2nd Ball Run Is: ",Opp_Team_SecondBall_Run)

        elif run2 == "No Ball":

                print("\nBall Is: ",run2)
                print("Extra Run Is: ",Noball2, "No Ball Attend By: ",reball2)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run2=random.choice((0,1,2,3,4,6))
                FreeHit2=Free_Run2

                No_Reball_II= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                if No_Reball_II == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit2)

                    Opp_Team_SecondBall_Run += Noball2+reball2+FreeHit2
                    print("\nTotal 2nd Ball Run Is: ",Opp_Team_SecondBall_Run)
            
        elif run2 == "Out":
                Opp_Team_SecondBall_Run += Out2
                print("\nYou Are: ",run2)
                print("\n2nd Ball Out Run Consider As: ",Out2)

        elif second_ball == "":
                print("\n2nd Ball Run: ",run2)
                Opp_Team_SecondBall_Run += run2
                
                
        else:
                print("\nEnter The Correct Number")


# -----------------------------THIRD BALL STARTS FROM-------------------------------------------------------------------------

        run_choice3=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
        run3=run_choice3

        reball_run3=random.choice((0,1,2,3,4,6))
        reball3=reball_run3

        Noball3=1
        Wide3=1
        Out3=0

        Opp_Team_ThirdBall_Run = 0
            
        third_ball=input("\nPress ( 'ENTER' ) To Deliver The Third Ball: ")

        if run3 == "Wide":
                print("\nBall Is: ",run3)
                print("Extra Run: ",Wide3)

                Reball_III=input("\nPress ( 'ENTER' ) Deliver The Reball: ")

                if Reball_III == "":
                    print("\nWide Reball Run: ",reball3)
                    
                    Opp_Team_ThirdBall_Run += Wide3+reball3
                    print("\nTotal 3rd Ball Run Is: ",Opp_Team_ThirdBall_Run)

        elif run3 == "No Ball":

                print("\nBall Is: ",run3)
                print("Extra Run Is: ",Noball3, "No Ball Attend By: ",reball3)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run3=random.choice((0,1,2,3,4,6))
                FreeHit3=Free_Run3

                No_Reball_III= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                if No_Reball_III == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit3)

                    Opp_Team_ThirdBall_Run += Noball3+reball3+FreeHit3
                    print("\nTotal 3rd Ball Run Is: ",Opp_Team_ThirdBall_Run)
            
        elif run3 == "Out":
                Opp_Team_ThirdBall_Run += Out3
                print("\nYou Are: ",run3)
                print("\n3rd Ball Out Run Consider As: ",Out3)

        elif third_ball == "":
                print("\n3rd Ball Run: ",run3)
                Opp_Team_ThirdBall_Run += run3
                
                
        else:
                print("\nEnter The Correct Number")

# -----------------------------FOURTH BALL STARTS FROM-------------------------------------------------------------------------

        run_choice4=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
        run4=run_choice4

        reball_run4=random.choice((0,1,2,3,4,6))
        reball4=reball_run4

        Noball4=1
        Wide4=1
        Out4=0

        Opp_Team_FourthBall_Run = 0
            
        fourth_ball=input("\nPress ( 'ENTER' ) To Deliver The Fourth Ball: ")

        if run4 == "Wide":
                print("\nBall Is: ",run4)
                print("Extra Run: ",Wide4)

                Reball_IV=input("\nPress ( 'ENTER' ) Deliver The Reball: ")

                if Reball_IV == "":
                    print("\nWide Reball Run: ",reball4)
                    
                    Opp_Team_FourthBall_Run += Wide4+reball4
                    print("\nTotal 4rd Ball Run Is: ",Opp_Team_FourthBall_Run)

        elif run4 == "No Ball":

                print("\nBall Is: ",run4)
                print("Extra Run Is: ",Noball4, "No Ball Attend By: ",reball4)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run4=random.choice((0,1,2,3,4,6))
                FreeHit4=Free_Run4

                No_Reball_IV= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                if No_Reball_IV == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit4)

                    Opp_Team_FourthBall_Run += Noball4+reball4+FreeHit4
                    print("\nTotal 4th Ball Run Is: ",Opp_Team_FourthBall_Run)
            
        elif run4 == "Out":
                Opp_Team_FourthBall_Run += Out4
                print("\nYou Are: ",run4)
                print("\n4th Ball Out Run Consider As: ",Out4)

        elif fourth_ball == "":
                print("\n4th Ball Run: ",run4)
                Opp_Team_FourthBall_Run += run4
                
                
        else:
                print("\nEnter The Correct Number")


# -----------------------------FIFTH BALL STARTS FROM-------------------------------------------------------------------------

        run_choice5=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
        run5=run_choice5

        reball_run5=random.choice((0,1,2,3,4,6))
        reball5=reball_run5

        Noball5=1
        Wide5=1
        Out5=0
        
        Opp_Team_FifthBall_Run = 0

        fifth_ball=input("\nPress ( 'ENTER' ) To Deliver The Fifth Ball: ")

        if run5 == "Wide":
                print("\nBall Is: ",run5)
                print("Extra Run: ",Wide5)

                Reball_V=input("\nPress ( 'ENTER' ) To Deliver The Reball: ")

                if Reball_V == "":
                    print("\nWide Reball Run: ",reball5)
                    
                    Opp_Team_FifthBall_Run += Wide5+reball5
                    print("\nTotal 5th Ball Run Is: ",Opp_Team_FifthBall_Run)

        elif run5 == "No Ball":

                print("\nBall Is: ",run5)
                print("Extra Run Is: ",Noball5, "No Ball Attend By: ",reball5)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run5=random.choice((0,1,2,3,4,6))
                FreeHit5=Free_Run5

                No_Reball_V= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                if No_Reball_V == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit5)

                    Opp_Team_FifthBall_Run += Noball5+reball5+FreeHit5
                    print("\nTotal 5th Ball Run Is: ",Opp_Team_FifthBall_Run)
            
        elif run5 == "Out":
                Opp_Team_FifthBall_Run += Out5
                print("\nYou Are: ",run5)
                print("\n5th Ball Out Run Consider As: ",Out5)

        elif fifth_ball == "":
                print("\n5th Ball Run: ",run5)
                Opp_Team_FifthBall_Run += run5
                
                
        else:
                print("\nEnter The Correct Number")


# -----------------------------SIXTH BALL STARTS FROM-------------------------------------------------------------------------

        run_choice6=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
        run6=run_choice6

        reball_run6=random.choice((0,1,2,3,4,6))
        reball6=reball_run6

        Noball6=1
        Wide6=1
        Out6=0

        Opp_Team_SixthBall_Run = 0
            
        sixth_ball=input("\nPress ( 'ENTER' ) To Deliver The Sixth Ball: ")

        if run6 == "Wide":
                print("\nBall Is: ",run6)
                print("Extra Run: ",Wide6)

                Reball_VI=input("\nPress ( 'ENTER' ) Reball ENTER 6: ")

                if Reball_VI == "":
                    print("\nWide Reball Run: ",reball6)
                    
                    Opp_Team_SixthBall_Run += Wide6+reball6
                    print("\nTotal 6th Ball Run Is: ",Opp_Team_SixthBall_Run)

        elif run6 == "No Ball":

                print("\nBall Is: ",run6)
                print("Extra Run Is: ",Noball6, "No Ball Attend By: ",reball6)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run6=random.choice((0,1,2,3,4,6))
                FreeHit6=Free_Run6

                No_Reball_VI= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                if No_Reball_VI == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit6)

                    Opp_Team_SixthBall_Run += Noball6+reball6+FreeHit6
                    print("\nTotal 6th Ball Run Is: ",Opp_Team_SixthBall_Run)
            
        elif run6 == "Out":
                Opp_Team_SixthBall_Run += Out6
                print("\nYou Are: ",run6)
                print("\n6th Ball Out Run Consider As: ",Out6)

        elif sixth_ball == "":
                print("\n6th Ball Run: ",run6)
                Opp_Team_SixthBall_Run += run6
                
                
        else:
                print("\nEnter The Correct Number")

        Opponent_Total = Opp_Team_FirstBall_Run + Opp_Team_SecondBall_Run + Opp_Team_ThirdBall_Run + Opp_Team_FourthBall_Run + Opp_Team_FifthBall_Run + Opp_Team_SixthBall_Run

#----------------------------------------First Batting TOTAL-------------------------------------------------------------------------
        print (f"\n{OPPONENT_TEAMS} TOTAL SCORE: ",Opponent_Total)
# ---------------------------------------A (MY TEAM) BATTING-------------------------------------------------------------------------

        run_choice=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
        run=run_choice

        reball_run=random.choice((0,1,2,3,4,6))
        reball=reball_run

        Noball=1
        Wide=1
        Out=0

        My_Team_FirstBall_Run = 0

        Beat=input(f"\t\nNOW ( {TEAMS} ) BATTING ... READY TO BEAT {OPPONENT_TEAMS} SCORE: ( -{Opponent_Total}- )\n\nIF YOU READY PRESS ( 'ENTER' ): ")

        first_ball=input("\nPress ( 'ENTER' ) To Face The First Ball: ")

        if run == "Wide":
                print("\nBall Is: ",run)
                print("Extra Run: ",Wide)

                Reball_I=input("\nPress ( 'ENTER' ) To Face The Reball: ")

                if Reball_I == "":
                    print("\nWide Reball Run: ",reball)
                    
                    My_Team_FirstBall_Run += Wide+reball
                    print("\nTotal 1st Ball Run Is: ",My_Team_FirstBall_Run)

        elif run == "No Ball":

                print("\nBall Is: ",run)
                print("Extra Run Is: ",Noball, "No Ball Attend By: ",reball)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run=random.choice((0,1,2,3,4,6))
                FreeHit=Free_Run

                No_Reball_I= input("Press ( 'ENTER' ) to Hit The FREE HIT BALL!!!: ")

                if No_Reball_I == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit)

                    My_Team_FirstBall_Run += Noball+reball+FreeHit
                    print("\nTotal 1st Ball Run Is: ",My_Team_FirstBall_Run)
            
        elif run == "Out":
                print("\nYou Are: ",run)
                print("\n1st Ball Out Consider As: ",Out)

        elif first_ball == "":
                My_Team_FirstBall_Run += run
                print("\n1st Ball Run: ",run)
                
                
        else:
                print("\nEnter The Correct Number")

# -----------------------------SECOND BALL STARTS FROM-------------------------------------------------------------------------

        run_choice2=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
        run2=run_choice2

        reball_run2=random.choice((0,1,2,3,4,6))
        reball2=reball_run2

        Noball2=1
        Wide2=1
        Out2=0

        My_Team_SecondBall_Run=0
            
        second_ball=input("\nPress ( 'ENTER' ) To Face The Second Ball: ")

        if run2 == "Wide":
                print("\nBall Is: ",run2)
                print("Extra Run: ",Wide2)

                Reball_II=input("\nPress ( 'ENTER' ) Face The Reball: ")

                if Reball_II == "":
                    print("\nWide Reball Run: ",reball2)
                    
                    My_Team_SecondBall_Run += Wide2+reball2
                    print("\nTotal 2nd Ball Run Is: ",My_Team_SecondBall_Run)

        elif run2 == "No Ball":

                print("\nBall Is: ",run2)
                print("Extra Run Is: ",Noball2, "No Ball Attend By: ",reball2)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run2=random.choice((0,1,2,3,4,6))
                FreeHit2=Free_Run2

                No_Reball_II= input("Press ( 'ENTER' ) to Hit The FREE HIT BALL!!!: ")

                if No_Reball_II == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit2)

                    My_Team_SecondBall_Run += Noball2+reball2+FreeHit2
                    print("\nTotal 2nd Ball Run Is: ",My_Team_SecondBall_Run)
            
        elif run2 == "Out":
                print("\nYou Are: ",run2)
                print("\n2nd Ball Out Run Consider As: ",Out2)

        elif second_ball == "":
                print("\n2nd Ball Run: ",run2)
                My_Team_SecondBall_Run += run2
                
                
        else:
                print("\nEnter The Correct Number")


# -----------------------------THIRD BALL STARTS FROM-------------------------------------------------------------------------

        run_choice3=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
        run3=run_choice3

        reball_run3=random.choice((0,1,2,3,4,6))
        reball3=reball_run3

        Noball3=1
        Wide3=1
        Out3=0

        My_Team_ThirdBall_Run=0
            
        third_ball=input("\nPress ( 'ENTER' ) To Face The Third Ball: ")

        if run3 == "Wide":
                print("\nBall Is: ",run3)
                print("Extra Run: ",Wide3)

                Reball_III=input("\nPress ( 'ENTER' ) Face The Reball: ")

                if Reball_III == "":
                    print("\nWide Reball Run: ",reball3)
                    
                    My_Team_ThirdBall_Run += Wide3+reball3
                    print("\nTotal 3rd Ball Run Is: ",My_Team_ThirdBall_Run)

        elif run3 == "No Ball":

                print("\nBall Is: ",run3)
                print("Extra Run Is: ",Noball3, "No Ball Attend By: ",reball3)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run3=random.choice((0,1,2,3,4,6))
                FreeHit3=Free_Run3

                No_Reball_III= input("Press ( 'ENTER' ) to Hit The FREE HIT BALL!!!: ")

                if No_Reball_III == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit3)

                    My_Team_ThirdBall_Run += Noball3+reball3+FreeHit3
                    print("\nTotal 3rd Ball Run Is: ",My_Team_ThirdBall_Run)
            
        elif run3 == "Out":
                print("\nYou Are: ",run3)
                print("\n3rd Ball Out Run Consider As: ",Out3)

        elif third_ball == "":
                print("\n3rd Ball Run: ",run3)
                My_Team_ThirdBall_Run += run3
                
                
        else:
                print("\nEnter The Correct Number")

# -----------------------------FOURTH BALL STARTS FROM-------------------------------------------------------------------------

        run_choice4=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
        run4=run_choice4

        reball_run4=random.choice((0,1,2,3,4,6))
        reball4=reball_run4

        Noball4=1
        Wide4=1
        Out4=0

        My_Team_FourthBall_Run=0
            
        fourth_ball=input("\nPress ( 'ENTER' ) To Face The Fourth Ball: ")

        if run4 == "Wide":
                print("\nBall Is: ",run4)
                print("Extra Run: ",Wide4)

                Reball_IV=input("\nPress ( 'ENTER' ) Face The Reball: ")

                if Reball_IV == "":
                    print("\nWide Reball Run: ",reball4)
                    
                    My_Team_FourthBall_Run += Wide4+reball4
                    print("\nTotal 4rd Ball Run Is: ",My_Team_FourthBall_Run)

        elif run4 == "No Ball":

                print("\nBall Is: ",run4)
                print("Extra Run Is: ",Noball4, "No Ball Attend By: ",reball4)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run4=random.choice((0,1,2,3,4,6))
                FreeHit4=Free_Run4

                No_Reball_IV= input("Press ( 'ENTER' ) to Hit The FREE HIT BALL!!!: ")

                if No_Reball_IV == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit4)

                    My_Team_FourthBall_Run += Noball4+reball4+FreeHit4
                    print("\nTotal 4th Ball Run Is: ",My_Team_FourthBall_Run)
            
        elif run4 == "Out":
                print("\nYou Are: ",run4)
                print("\n4th Ball Out Run Consider As: ",Out4)

        elif fourth_ball == "":
                print("\n4th Ball Run: ",run4)
                My_Team_FourthBall_Run += run4
                
                
        else:
                print("\nEnter The Correct Number")


# -----------------------------FIFTH BALL STARTS FROM-------------------------------------------------------------------------

        run_choice5=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
        run5=run_choice5

        reball_run5=random.choice((0,1,2,3,4,6))
        reball5=reball_run5

        Noball5=1
        Wide5=1
        Out5=0

        My_Team_FifthBall_Run=0
            
        fifth_ball=input("\nPress ( 'ENTER' ) To Face The Fifth Ball: ")

        if run5 == "Wide":
                print("\nBall Is: ",run5)
                print("Extra Run: ",Wide5)

                Reball_V=input("\nPress ( 'ENTER' ) To Face The Reball: ")

                if Reball_V == "":
                    print("\nWide Reball Run: ",reball5)
                    
                    My_Team_FifthBall_Run += Wide5+reball5
                    print("\nTotal 5th Ball Run Is: ",My_Team_FifthBall_Run)

        elif run5 == "No Ball":

                print("\nBall Is: ",run5)
                print("Extra Run Is: ",Noball5, "No Ball Attend By: ",reball5)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run5=random.choice((0,1,2,3,4,6))
                FreeHit5=Free_Run5

                No_Reball_V= input("Press ( 'ENTER' ) to Hit The FREE HIT BALL!!!: ")

                if No_Reball_V == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit5)

                    My_Team_FifthBall_Run += Noball5+reball5+FreeHit5
                    print("\nTotal 5th Ball Run Is: ",My_Team_FifthBall_Run)
            
        elif run5 == "Out":
                print("\nYou Are: ",run5)
                print("\n5th Ball Out Run Consider As: ",Out5)

        elif fifth_ball == "":
                print("\n5th Ball Run: ",run5)
                My_Team_FifthBall_Run += run5
                
                
        else:
                print("\nEnter The Correct Number")


# -----------------------------SIXTH BALL STARTS FROM-------------------------------------------------------------------------

        run_choice6=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
        run6=run_choice6

        reball_run6=random.choice((0,1,2,3,4,6))
        reball6=reball_run6

        Noball6=1
        Wide6=1
        Out6=0

        My_Team_SixthBall_Run=0
            
        sixth_ball=input("\nPress ( 'ENTER' ) To Face The Sixth Ball: ")

        if run6 == "Wide":
                print("\nBall Is: ",run6)
                print("Extra Run: ",Wide6)

                Reball_VI=input("\nPress ( 'ENTER' ) Face The Reball: ")

                if Reball_VI == "":
                    print("\nWide Reball Run: ",reball6)
                    
                    My_Team_SixthBall_Run += Wide6+reball6
                    print("\nTotal 6th Ball Run Is: ",My_Team_SixthBall_Run)

        elif run6 == "No Ball":

                print("\nBall Is: ",run6)
                print("Extra Run Is: ",Noball6, "No Ball Attend By: ",reball6)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run6=random.choice((0,1,2,3,4,6))
                FreeHit6=Free_Run6

                No_Reball_VI= input("Press ( 'ENTER' ) to Hit The FREE HIT BALL!!!: ")

                if No_Reball_VI == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit6)

                    My_Team_SixthBall_Run += Noball6+reball6+FreeHit6
                    print("\nTotal 6th Ball Run Is: ",My_Team_SixthBall_Run)
            
        elif run6 == "Out":
                print("\nYou Are: ",run6)
                print("\n6th Ball Out Run Consider As: ",Out6)

        elif sixth_ball == "":
                print("\n6th Ball Run: ",run6)
                My_Team_SixthBall_Run += run6
                
                
        else:
                print("\nEnter The Correct Number")


        MyTeam_Total = My_Team_FirstBall_Run + My_Team_SecondBall_Run + My_Team_ThirdBall_Run + My_Team_FourthBall_Run + My_Team_FifthBall_Run + My_Team_SixthBall_Run

#----------------------------------------First Batting TOTAL-------------------------------------------------------------------------
        
        print (f"\n{TEAMS} TOTAL SCORE: ",MyTeam_Total)
        
#--------------------------------------MATCH RESULT------------------------------------------------------------------------

        Opponent_Result = Opponent_Total - MyTeam_Total
        MyTeam_Result = MyTeam_Total - Opponent_Total

        if Opponent_Total > MyTeam_Total:
             
             print (f"\n\tMATCH WIN BY {OPPONENT_TEAMS} WITH ( {Opponent_Result} ) RUN DIFFRENCE !!!")
             break

        elif Opponent_Total < MyTeam_Total:
             
             print (f"\n\tMATCH WIN BY {TEAMS} WITH ( {MyTeam_Result} ) RUN DIFFRENCE !!!")
             break

# ********************************A(OUR TEAM) TEAM BATTING********************************************************************

    elif Yours == "HEADS" and Toss == "HEADS" or Yours == "TAILS" and Toss == "TAILS":

        BAT_BOWL=input(f"Toss Win By {TEAMS}\n\nCHOOSE BAT(1) OR BOWL(2): ").upper()

        if BAT_BOWL == "BAT" or BAT_BOWL == "1":
            
            run_choice=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
            run=run_choice

            reball_run=random.choice((0,1,2,3,4,6))
            reball=reball_run

            Noball=1
            Wide=1
            Out=0

            My_Team_FirstBall_Run = 0

            first_ball=input("\nPress ( 'ENTER' ) To Face The First Ball: ")

            if run == "Wide":
                    print("\nBall Is: ",run)
                    print("Extra Run: ",Wide)

                    Reball_I=input("\nPress ( 'ENTER' ) To Face The Reball: ")

                    if Reball_I == "":
                        print("\nWide Reball Run: ",reball)
                        
                        My_Team_FirstBall_Run += Wide+reball
                        print("\nTotal 1st Ball Run Is: ",My_Team_FirstBall_Run)

            elif run == "No Ball":

                    print("\nBall Is: ",run)
                    print("Extra Run Is: ",Noball, "No Ball Attend By: ",reball)
                    
                    print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                    
                    Free_Run=random.choice((0,1,2,3,4,6))
                    FreeHit=Free_Run

                    No_Reball_I= input("Press ( 'ENTER' ) to Hit The FREE HIT BALL!!!: ")

                    if No_Reball_I == "":
                        print("\nFREE HIT!!! Hit By: ",FreeHit)

                        My_Team_FirstBall_Run += Noball+reball+FreeHit
                        print("\nTotal 1st Ball Run Is: ",My_Team_FirstBall_Run)
                
            elif run == "Out":
                    print("\nYou Are: ",run)
                    print("\n1st Ball Out Consider As: ",Out)

            elif first_ball == "":
                    My_Team_FirstBall_Run += run
                    print("\n1st Ball Run: ",run)
                    
                    
            else:
                    print("\nEnter The Correct Number")

    # -----------------------------SECOND BALL STARTS FROM-------------------------------------------------------------------------

            run_choice2=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
            run2=run_choice2

            reball_run2=random.choice((0,1,2,3,4,6))
            reball2=reball_run2

            Noball2=1
            Wide2=1
            Out2=0

            My_Team_SecondBall_Run=0
                
            second_ball=input("\nPress ( 'ENTER' ) To Face The Second Ball: ")

            if run2 == "Wide":
                    print("\nBall Is: ",run2)
                    print("Extra Run: ",Wide2)

                    Reball_II=input("\nPress ( 'ENTER' ) Face The Reball: ")

                    if Reball_II == "":
                        print("\nWide Reball Run: ",reball2)
                        
                        My_Team_SecondBall_Run += Wide2+reball2
                        print("\nTotal 2nd Ball Run Is: ",My_Team_SecondBall_Run)

            elif run2 == "No Ball":

                    print("\nBall Is: ",run2)
                    print("Extra Run Is: ",Noball2, "No Ball Attend By: ",reball2)
                    
                    print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                    
                    Free_Run2=random.choice((0,1,2,3,4,6))
                    FreeHit2=Free_Run2

                    No_Reball_II= input("Press ( 'ENTER' ) to Hit The FREE HIT BALL!!!: ")

                    if No_Reball_II == "":
                        print("\nFREE HIT!!! Hit By: ",FreeHit2)

                        My_Team_SecondBall_Run += Noball2+reball2+FreeHit2
                        print("\nTotal 2nd Ball Run Is: ",My_Team_SecondBall_Run)
                
            elif run2 == "Out":
                    print("\nYou Are: ",run2)
                    print("\n2nd Ball Out Run Consider As: ",Out2)

            elif second_ball == "":
                    print("\n2nd Ball Run: ",run2)
                    My_Team_SecondBall_Run += run2
                    
                    
            else:
                    print("\nEnter The Correct Number")


    # -----------------------------THIRD BALL STARTS FROM-------------------------------------------------------------------------

            run_choice3=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
            run3=run_choice3

            reball_run3=random.choice((0,1,2,3,4,6))
            reball3=reball_run3

            Noball3=1
            Wide3=1
            Out3=0

            My_Team_ThirdBall_Run=0
                
            third_ball=input("\nPress ( 'ENTER' ) To Face The Third Ball: ")

            if run3 == "Wide":
                    print("\nBall Is: ",run3)
                    print("Extra Run: ",Wide3)

                    Reball_III=input("\nPress ( 'ENTER' ) Face The Reball: ")

                    if Reball_III == "":
                        print("\nWide Reball Run: ",reball3)
                        
                        My_Team_ThirdBall_Run += Wide3+reball3
                        print("\nTotal 3rd Ball Run Is: ",My_Team_ThirdBall_Run)

            elif run3 == "No Ball":

                    print("\nBall Is: ",run3)
                    print("Extra Run Is: ",Noball3, "No Ball Attend By: ",reball3)
                    
                    print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                    
                    Free_Run3=random.choice((0,1,2,3,4,6))
                    FreeHit3=Free_Run3

                    No_Reball_III= input("Press ( 'ENTER' ) to Hit The FREE HIT BALL!!!: ")

                    if No_Reball_III == "":
                        print("\nFREE HIT!!! Hit By: ",FreeHit3)

                        My_Team_ThirdBall_Run += Noball3+reball3+FreeHit3
                        print("\nTotal 3rd Ball Run Is: ",My_Team_ThirdBall_Run)
                
            elif run3 == "Out":
                    print("\nYou Are: ",run3)
                    print("\n3rd Ball Out Run Consider As: ",Out3)

            elif third_ball == "":
                    print("\n3rd Ball Run: ",run3)
                    My_Team_ThirdBall_Run += run3
                    
                    
            else:
                    print("\nEnter The Correct Number")

    # -----------------------------FOURTH BALL STARTS FROM-------------------------------------------------------------------------

            run_choice4=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
            run4=run_choice4

            reball_run4=random.choice((0,1,2,3,4,6))
            reball4=reball_run4

            Noball4=1
            Wide4=1
            Out4=0

            My_Team_FourthBall_Run=0
                
            fourth_ball=input("\nPress ( 'ENTER' ) To Face The Fourth Ball: ")

            if run4 == "Wide":
                    print("\nBall Is: ",run4)
                    print("Extra Run: ",Wide4)

                    Reball_IV=input("\nPress ( 'ENTER' ) Face The Reball: ")

                    if Reball_IV == "":
                        print("\nWide Reball Run: ",reball4)
                        
                        My_Team_FourthBall_Run += Wide4+reball4
                        print("\nTotal 4rd Ball Run Is: ",My_Team_FourthBall_Run)

            elif run4 == "No Ball":

                    print("\nBall Is: ",run4)
                    print("Extra Run Is: ",Noball4, "No Ball Attend By: ",reball4)
                    
                    print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                    
                    Free_Run4=random.choice((0,1,2,3,4,6))
                    FreeHit4=Free_Run4

                    No_Reball_IV= input("Press ( 'ENTER' ) to Hit The FREE HIT BALL!!!: ")

                    if No_Reball_IV == "":
                        print("\nFREE HIT!!! Hit By: ",FreeHit4)

                        My_Team_FourthBall_Run += Noball4+reball4+FreeHit4
                        print("\nTotal 4th Ball Run Is: ",My_Team_FourthBall_Run)
                
            elif run4 == "Out":
                    print("\nYou Are: ",run4)
                    print("\n4th Ball Out Run Consider As: ",Out4)

            elif fourth_ball == "":
                    print("\n4th Ball Run: ",run4)
                    My_Team_FourthBall_Run += run4
                    
                    
            else:
                    print("\nEnter The Correct Number")


    # -----------------------------FIFTH BALL STARTS FROM-------------------------------------------------------------------------

            run_choice5=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
            run5=run_choice5

            reball_run5=random.choice((0,1,2,3,4,6))
            reball5=reball_run5

            Noball5=1
            Wide5=1
            Out5=0

            My_Team_FifthBall_Run=0
                
            fifth_ball=input("\nPress ( 'ENTER' ) To Face The Fifth Ball: ")

            if run5 == "Wide":
                    print("\nBall Is: ",run5)
                    print("Extra Run: ",Wide5)

                    Reball_V=input("\nPress ( 'ENTER' ) To Face The Reball: ")

                    if Reball_V == "":
                        print("\nWide Reball Run: ",reball5)
                        
                        My_Team_FifthBall_Run += Wide5+reball5
                        print("\nTotal 5th Ball Run Is: ",My_Team_FifthBall_Run)

            elif run5 == "No Ball":

                    print("\nBall Is: ",run5)
                    print("Extra Run Is: ",Noball5, "No Ball Attend By: ",reball5)
                    
                    print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                    
                    Free_Run5=random.choice((0,1,2,3,4,6))
                    FreeHit5=Free_Run5

                    No_Reball_V= input("Press ( 'ENTER' ) to Hit The FREE HIT BALL!!!: ")

                    if No_Reball_V == "":
                        print("\nFREE HIT!!! Hit By: ",FreeHit5)

                        My_Team_FifthBall_Run += Noball5+reball5+FreeHit5
                        print("\nTotal 5th Ball Run Is: ",My_Team_FifthBall_Run)
                
            elif run5 == "Out":
                    print("\nYou Are: ",run5)
                    print("\n5th Ball Out Run Consider As: ",Out5)

            elif fifth_ball == "":
                    print("\n5th Ball Run: ",run5)
                    My_Team_FifthBall_Run += run5
                    
                    
            else:
                    print("\nEnter The Correct Number")


    # -----------------------------SIXTH BALL STARTS FROM-------------------------------------------------------------------------

            run_choice6=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
            run6=run_choice6

            reball_run6=random.choice((0,1,2,3,4,6))
            reball6=reball_run6

            Noball6=1
            Wide6=1
            Out6=0

            My_Team_SixthBall_Run=0
                
            sixth_ball=input("\nPress ( 'ENTER' ) To Face The Sixth Ball: ")

            if run6 == "Wide":
                    print("\nBall Is: ",run6)
                    print("Extra Run: ",Wide6)

                    Reball_VI=input("\nPress ( 'ENTER' ) Face The Reball: ")

                    if Reball_VI == "":
                        print("\nWide Reball Run: ",reball6)
                        
                        My_Team_SixthBall_Run += Wide6+reball6
                        print("\nTotal 6th Ball Run Is: ",My_Team_SixthBall_Run)

            elif run6 == "No Ball":

                    print("\nBall Is: ",run6)
                    print("Extra Run Is: ",Noball6, "No Ball Attend By: ",reball6)
                    
                    print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                    
                    Free_Run6=random.choice((0,1,2,3,4,6))
                    FreeHit6=Free_Run6

                    No_Reball_VI= input("Press ( 'ENTER' ) to Hit The FREE HIT BALL!!!: ")

                    if No_Reball_VI == "":
                        print("\nFREE HIT!!! Hit By: ",FreeHit6)

                        My_Team_SixthBall_Run += Noball6+reball6+FreeHit6
                        print("\nTotal 6th Ball Run Is: ",My_Team_SixthBall_Run)
                
            elif run6 == "Out":
                    print("\nYou Are: ",run6)
                    print("\n6th Ball Out Run Consider As: ",Out6)

            elif sixth_ball == "":
                    print("\n6th Ball Run: ",run6)
                    My_Team_SixthBall_Run += run6
                    
                    
            else:
                    print("\nEnter The Correct Number")


            MyTeam_Total = My_Team_FirstBall_Run + My_Team_SecondBall_Run + My_Team_ThirdBall_Run + My_Team_FourthBall_Run + My_Team_FifthBall_Run + My_Team_SixthBall_Run

#----------------------------------------First Batting TOTAL-------------------------------------------------------------------------
        
            print (f"\n{TEAMS} TOTAL SCORE: ",MyTeam_Total)

#-----------------------------A(OPPONENT BATTING)---------------------------------------------------------------------------------

            Beat=input(f"\t\nNOW ( {OPPONENT_TEAMS} ) BATTING ... READY TO BEAT {TEAMS} SCORE: ( -{MyTeam_Total}- )\n\nIF YOU READY PRESS ( 'ENTER' ): ")

            first_ball=input("\nPress ( 'ENTER' ) To Deliver The First Ball: ")

        if run == "Wide":
                print("\nBall Is: ",run)
                print("Extra Run: ",Wide)

                Reball_I=input("\nPress ( 'ENTER' ) To Deliver The Reball: ")

                if Reball_I == "":
                    print("\nWide Reball Run: ",reball)
                    
                    Opp_Team_FirstBall_Run += Wide+reball


                    print("\nTotal 1st Ball Run Is: ",Opp_Team_FirstBall_Run)

        elif run == "No Ball":

                print("\nBall Is: ",run)
                print("Extra Run Is: ",Noball, "No Ball Attend By: ",reball)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run=random.choice((0,1,2,3,4,6))
                FreeHit=Free_Run

                No_Reball_I= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                if No_Reball_I == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit)

                    Opp_Team_FirstBall_Run += Noball+reball+FreeHit
                    print("\nTotal 1st Ball Run Is: ",Opp_Team_FirstBall_Run)
            
        elif run == "Out":
                Opp_Team_FirstBall_Run += Out
                print("\nYou Are: ",run)
                print("\n1st Ball Out Consider As: ",Out)

        elif first_ball == "":
                Opp_Team_FirstBall_Run += run
                print("\n1st Ball Run: ",run)
                
                
        else:
                print("\nEnter The Correct Number")

# -----------------------------SECOND BALL STARTS FROM-------------------------------------------------------------------------

        run_choice2=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
        run2=run_choice2

        reball_run2=random.choice((0,1,2,3,4,6))
        reball2=reball_run2

        Noball2=1
        Wide2=1
        Out2=0

        Opp_Team_SecondBall_Run = 0
            
        second_ball=input("\nPress ( 'ENTER' ) To Deliver The Second Ball: ")

        if run2 == "Wide":
                print("\nBall Is: ",run2)
                print("Extra Run: ",Wide2)

                Reball_II=input("\nPress ( 'ENTER' ) Deliver The Reball: ")

                if Reball_II == "":
                    print("\nWide Reball Run: ",reball2)
                    
                    Opp_Team_SecondBall_Run += Wide2+reball2
                    print("\nTotal 2nd Ball Run Is: ",Opp_Team_SecondBall_Run)

        elif run2 == "No Ball":

                print("\nBall Is: ",run2)
                print("Extra Run Is: ",Noball2, "No Ball Attend By: ",reball2)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run2=random.choice((0,1,2,3,4,6))
                FreeHit2=Free_Run2

                No_Reball_II= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                if No_Reball_II == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit2)

                    Opp_Team_SecondBall_Run += Noball2+reball2+FreeHit2
                    print("\nTotal 2nd Ball Run Is: ",Opp_Team_SecondBall_Run)
            
        elif run2 == "Out":
                Opp_Team_SecondBall_Run += Out2
                print("\nYou Are: ",run2)
                print("\n2nd Ball Out Run Consider As: ",Out2)

        elif second_ball == "":
                print("\n2nd Ball Run: ",run2)
                Opp_Team_SecondBall_Run += run2
                
                
        else:
                print("\nEnter The Correct Number")


# -----------------------------THIRD BALL STARTS FROM-------------------------------------------------------------------------

        run_choice3=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
        run3=run_choice3

        reball_run3=random.choice((0,1,2,3,4,6))
        reball3=reball_run3

        Noball3=1
        Wide3=1
        Out3=0

        Opp_Team_ThirdBall_Run = 0
            
        third_ball=input("\nPress ( 'ENTER' ) To Deliver The Third Ball: ")

        if run3 == "Wide":
                print("\nBall Is: ",run3)
                print("Extra Run: ",Wide3)

                Reball_III=input("\nPress ( 'ENTER' ) Deliver The Reball: ")

                if Reball_III == "":
                    print("\nWide Reball Run: ",reball3)
                    
                    Opp_Team_ThirdBall_Run += Wide3+reball3
                    print("\nTotal 3rd Ball Run Is: ",Opp_Team_ThirdBall_Run)

        elif run3 == "No Ball":

                print("\nBall Is: ",run3)
                print("Extra Run Is: ",Noball3, "No Ball Attend By: ",reball3)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run3=random.choice((0,1,2,3,4,6))
                FreeHit3=Free_Run3

                No_Reball_III= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                if No_Reball_III == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit3)

                    Opp_Team_ThirdBall_Run += Noball3+reball3+FreeHit3
                    print("\nTotal 3rd Ball Run Is: ",Opp_Team_ThirdBall_Run)
            
        elif run3 == "Out":
                Opp_Team_ThirdBall_Run += Out3
                print("\nYou Are: ",run3)
                print("\n3rd Ball Out Run Consider As: ",Out3)

        elif third_ball == "":
                print("\n3rd Ball Run: ",run3)
                Opp_Team_ThirdBall_Run += run3
                
                
        else:
                print("\nEnter The Correct Number")

# -----------------------------FOURTH BALL STARTS FROM-------------------------------------------------------------------------

        run_choice4=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
        run4=run_choice4

        reball_run4=random.choice((0,1,2,3,4,6))
        reball4=reball_run4

        Noball4=1
        Wide4=1
        Out4=0

        Opp_Team_FourthBall_Run = 0
            
        fourth_ball=input("\nPress ( 'ENTER' ) To Deliver The Fourth Ball: ")

        if run4 == "Wide":
                print("\nBall Is: ",run4)
                print("Extra Run: ",Wide4)

                Reball_IV=input("\nPress ( 'ENTER' ) Deliver The Reball: ")

                if Reball_IV == "":
                    print("\nWide Reball Run: ",reball4)
                    
                    Opp_Team_FourthBall_Run += Wide4+reball4
                    print("\nTotal 4rd Ball Run Is: ",Opp_Team_FourthBall_Run)

        elif run4 == "No Ball":

                print("\nBall Is: ",run4)
                print("Extra Run Is: ",Noball4, "No Ball Attend By: ",reball4)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run4=random.choice((0,1,2,3,4,6))
                FreeHit4=Free_Run4

                No_Reball_IV= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                if No_Reball_IV == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit4)

                    Opp_Team_FourthBall_Run += Noball4+reball4+FreeHit4
                    print("\nTotal 4th Ball Run Is: ",Opp_Team_FourthBall_Run)
            
        elif run4 == "Out":
                Opp_Team_FourthBall_Run += Out4
                print("\nYou Are: ",run4)
                print("\n4th Ball Out Run Consider As: ",Out4)

        elif fourth_ball == "":
                print("\n4th Ball Run: ",run4)
                Opp_Team_FourthBall_Run += run4
                
                
        else:
                print("\nEnter The Correct Number")


# -----------------------------FIFTH BALL STARTS FROM-------------------------------------------------------------------------

        run_choice5=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
        run5=run_choice5

        reball_run5=random.choice((0,1,2,3,4,6))
        reball5=reball_run5

        Noball5=1
        Wide5=1
        Out5=0
        
        Opp_Team_FifthBall_Run = 0

        fifth_ball=input("\nPress ( 'ENTER' ) To Deliver The Fifth Ball: ")

        if run5 == "Wide":
                print("\nBall Is: ",run5)
                print("Extra Run: ",Wide5)

                Reball_V=input("\nPress ( 'ENTER' ) To Deliver The Reball: ")

                if Reball_V == "":
                    print("\nWide Reball Run: ",reball5)
                    
                    Opp_Team_FifthBall_Run += Wide5+reball5
                    print("\nTotal 5th Ball Run Is: ",Opp_Team_FifthBall_Run)

        elif run5 == "No Ball":

                print("\nBall Is: ",run5)
                print("Extra Run Is: ",Noball5, "No Ball Attend By: ",reball5)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run5=random.choice((0,1,2,3,4,6))
                FreeHit5=Free_Run5

                No_Reball_V= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                if No_Reball_V == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit5)

                    Opp_Team_FifthBall_Run += Noball5+reball5+FreeHit5
                    print("\nTotal 5th Ball Run Is: ",Opp_Team_FifthBall_Run)
            
        elif run5 == "Out":
                Opp_Team_FifthBall_Run += Out5
                print("\nYou Are: ",run5)
                print("\n5th Ball Out Run Consider As: ",Out5)

        elif fifth_ball == "":
                print("\n5th Ball Run: ",run5)
                Opp_Team_FifthBall_Run += run5
                
                
        else:
                print("\nEnter The Correct Number")


# -----------------------------SIXTH BALL STARTS FROM-------------------------------------------------------------------------

        run_choice6=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
        run6=run_choice6

        reball_run6=random.choice((0,1,2,3,4,6))
        reball6=reball_run6

        Noball6=1
        Wide6=1
        Out6=0

        Opp_Team_SixthBall_Run = 0
            
        sixth_ball=input("\nPress ( 'ENTER' ) To Deliver The Sixth Ball: ")

        if run6 == "Wide":
                print("\nBall Is: ",run6)
                print("Extra Run: ",Wide6)

                Reball_VI=input("\nPress ( 'ENTER' ) Reball ENTER 6: ")

                if Reball_VI == "":
                    print("\nWide Reball Run: ",reball6)
                    
                    Opp_Team_SixthBall_Run += Wide6+reball6
                    print("\nTotal 6th Ball Run Is: ",Opp_Team_SixthBall_Run)

        elif run6 == "No Ball":

                print("\nBall Is: ",run6)
                print("Extra Run Is: ",Noball6, "No Ball Attend By: ",reball6)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run6=random.choice((0,1,2,3,4,6))
                FreeHit6=Free_Run6

                No_Reball_VI= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                if No_Reball_VI == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit6)

                    Opp_Team_SixthBall_Run += Noball6+reball6+FreeHit6
                    print("\nTotal 6th Ball Run Is: ",Opp_Team_SixthBall_Run)
            
        elif run6 == "Out":
                Opp_Team_SixthBall_Run += Out6
                print("\nYou Are: ",run6)
                print("\n6th Ball Out Run Consider As: ",Out6)

        elif sixth_ball == "":
                print("\n6th Ball Run: ",run6)
                Opp_Team_SixthBall_Run += run6
                
                
        else:
                print("\nEnter The Correct Number")

        Opponent_Total = Opp_Team_FirstBall_Run + Opp_Team_SecondBall_Run + Opp_Team_ThirdBall_Run + Opp_Team_FourthBall_Run + Opp_Team_FifthBall_Run + Opp_Team_SixthBall_Run

#----------------------------------------First Batting TOTAL-------------------------------------------------------------------------
       
        print (f"\n{OPPONENT_TEAMS} TOTAL SCORE: ",Opponent_Total)

#--------------------------------------MATCH RESULT------------------------------------------------------------------------

        Opponent_Result = Opponent_Total - MyTeam_Total
        MyTeam_Result = MyTeam_Total - Opponent_Total

        if Opponent_Total > MyTeam_Total:
             
             print (f"\n\tMATCH WIN BY {OPPONENT_TEAMS} WITH ( {Opponent_Result} ) RUN DIFFRENCE !!!")
             break

        elif Opponent_Total < MyTeam_Total:
             
             print (f"\n\tMATCH WIN BY {TEAMS} WITH ( {MyTeam_Result} ) RUN DIFFRENCE !!!")
             break


# # ********************************B(OPPONENT) TEAM BOWLOING********************************************************************


        elif BAT_BOWL == "BOWL" or BAT_BOWL == "2":
            
            first_ball=input("\nPress ( 'ENTER' ) To Deliver The First Ball: ")

            if run == "Wide":
                    print("\nBall Is: ",run)
                    print("Extra Run: ",Wide)

                    Reball_I=input("\nPress ( 'ENTER' ) To Deliver The Reball: ")

                    if Reball_I == "":
                        print("\nWide Reball Run: ",reball)
                        
                        Opp_Team_FirstBall_Run += Wide+reball


                        print("\nTotal 1st Ball Run Is: ",Opp_Team_FirstBall_Run)

            elif run == "No Ball":

                    print("\nBall Is: ",run)
                    print("Extra Run Is: ",Noball, "No Ball Attend By: ",reball)
                    
                    print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                    
                    Free_Run=random.choice((0,1,2,3,4,6))
                    FreeHit=Free_Run

                    No_Reball_I= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                    if No_Reball_I == "":
                        print("\nFREE HIT!!! Hit By: ",FreeHit)

                        Opp_Team_FirstBall_Run += Noball+reball+FreeHit
                        print("\nTotal 1st Ball Run Is: ",Opp_Team_FirstBall_Run)
                
            elif run == "Out":
                    Opp_Team_FirstBall_Run += Out
                    print("\nYou Are: ",run)
                    print("\n1st Ball Out Consider As: ",Out)

            elif first_ball == "":
                    Opp_Team_FirstBall_Run += run
                    print("\n1st Ball Run: ",run)
                    
                    
            else:
                    print("\nEnter The Correct Number")

    # -----------------------------SECOND BALL STARTS FROM-------------------------------------------------------------------------

            run_choice2=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
            run2=run_choice2

            reball_run2=random.choice((0,1,2,3,4,6))
            reball2=reball_run2

            Noball2=1
            Wide2=1
            Out2=0

            Opp_Team_SecondBall_Run = 0
                
            second_ball=input("\nPress ( 'ENTER' ) To Deliver The Second Ball: ")

            if run2 == "Wide":
                    print("\nBall Is: ",run2)
                    print("Extra Run: ",Wide2)

                    Reball_II=input("\nPress ( 'ENTER' ) Deliver The Reball: ")

                    if Reball_II == "":
                        print("\nWide Reball Run: ",reball2)
                        
                        Opp_Team_SecondBall_Run += Wide2+reball2
                        print("\nTotal 2nd Ball Run Is: ",Opp_Team_SecondBall_Run)

            elif run2 == "No Ball":

                    print("\nBall Is: ",run2)
                    print("Extra Run Is: ",Noball2, "No Ball Attend By: ",reball2)
                    
                    print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                    
                    Free_Run2=random.choice((0,1,2,3,4,6))
                    FreeHit2=Free_Run2

                    No_Reball_II= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                    if No_Reball_II == "":
                        print("\nFREE HIT!!! Hit By: ",FreeHit2)

                        Opp_Team_SecondBall_Run += Noball2+reball2+FreeHit2
                        print("\nTotal 2nd Ball Run Is: ",Opp_Team_SecondBall_Run)
                
            elif run2 == "Out":
                    Opp_Team_SecondBall_Run += Out2
                    print("\nYou Are: ",run2)
                    print("\n2nd Ball Out Run Consider As: ",Out2)

            elif second_ball == "":
                    print("\n2nd Ball Run: ",run2)
                    Opp_Team_SecondBall_Run += run2
                    
                    
            else:
                    print("\nEnter The Correct Number")


    # -----------------------------THIRD BALL STARTS FROM-------------------------------------------------------------------------

            run_choice3=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
            run3=run_choice3

            reball_run3=random.choice((0,1,2,3,4,6))
            reball3=reball_run3

            Noball3=1
            Wide3=1
            Out3=0

            Opp_Team_ThirdBall_Run = 0
                
            third_ball=input("\nPress ( 'ENTER' ) To Deliver The Third Ball: ")

            if run3 == "Wide":
                    print("\nBall Is: ",run3)
                    print("Extra Run: ",Wide3)

                    Reball_III=input("\nPress ( 'ENTER' ) Deliver The Reball: ")

                    if Reball_III == "":
                        print("\nWide Reball Run: ",reball3)
                        
                        Opp_Team_ThirdBall_Run += Wide3+reball3
                        print("\nTotal 3rd Ball Run Is: ",Opp_Team_ThirdBall_Run)

            elif run3 == "No Ball":

                    print("\nBall Is: ",run3)
                    print("Extra Run Is: ",Noball3, "No Ball Attend By: ",reball3)
                    
                    print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                    
                    Free_Run3=random.choice((0,1,2,3,4,6))
                    FreeHit3=Free_Run3

                    No_Reball_III= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                    if No_Reball_III == "":
                        print("\nFREE HIT!!! Hit By: ",FreeHit3)

                        Opp_Team_ThirdBall_Run += Noball3+reball3+FreeHit3
                        print("\nTotal 3rd Ball Run Is: ",Opp_Team_ThirdBall_Run)
                
            elif run3 == "Out":
                    Opp_Team_ThirdBall_Run += Out3
                    print("\nYou Are: ",run3)
                    print("\n3rd Ball Out Run Consider As: ",Out3)

            elif third_ball == "":
                    print("\n3rd Ball Run: ",run3)
                    Opp_Team_ThirdBall_Run += run3
                    
                    
            else:
                    print("\nEnter The Correct Number")

    # -----------------------------FOURTH BALL STARTS FROM-------------------------------------------------------------------------

            run_choice4=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
            run4=run_choice4

            reball_run4=random.choice((0,1,2,3,4,6))
            reball4=reball_run4

            Noball4=1
            Wide4=1
            Out4=0

            Opp_Team_FourthBall_Run = 0
                
            fourth_ball=input("\nPress ( 'ENTER' ) To Deliver The Fourth Ball: ")

            if run4 == "Wide":
                    print("\nBall Is: ",run4)
                    print("Extra Run: ",Wide4)

                    Reball_IV=input("\nPress ( 'ENTER' ) Deliver The Reball: ")

                    if Reball_IV == "":
                        print("\nWide Reball Run: ",reball4)
                        
                        Opp_Team_FourthBall_Run += Wide4+reball4
                        print("\nTotal 4rd Ball Run Is: ",Opp_Team_FourthBall_Run)

            elif run4 == "No Ball":

                    print("\nBall Is: ",run4)
                    print("Extra Run Is: ",Noball4, "No Ball Attend By: ",reball4)
                    
                    print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                    
                    Free_Run4=random.choice((0,1,2,3,4,6))
                    FreeHit4=Free_Run4

                    No_Reball_IV= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                    if No_Reball_IV == "":
                        print("\nFREE HIT!!! Hit By: ",FreeHit4)

                        Opp_Team_FourthBall_Run += Noball4+reball4+FreeHit4
                        print("\nTotal 4th Ball Run Is: ",Opp_Team_FourthBall_Run)
                
            elif run4 == "Out":
                    Opp_Team_FourthBall_Run += Out4
                    print("\nYou Are: ",run4)
                    print("\n4th Ball Out Run Consider As: ",Out4)

            elif fourth_ball == "":
                    print("\n4th Ball Run: ",run4)
                    Opp_Team_FourthBall_Run += run4
                    
                    
            else:
                    print("\nEnter The Correct Number")


    # -----------------------------FIFTH BALL STARTS FROM-------------------------------------------------------------------------

            run_choice5=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
            run5=run_choice5

            reball_run5=random.choice((0,1,2,3,4,6))
            reball5=reball_run5

            Noball5=1
            Wide5=1
            Out5=0
            
            Opp_Team_FifthBall_Run = 0

            fifth_ball=input("\nPress ( 'ENTER' ) To Deliver The Fifth Ball: ")

            if run5 == "Wide":
                    print("\nBall Is: ",run5)
                    print("Extra Run: ",Wide5)

                    Reball_V=input("\nPress ( 'ENTER' ) To Deliver The Reball: ")

                    if Reball_V == "":
                        print("\nWide Reball Run: ",reball5)
                        
                        Opp_Team_FifthBall_Run += Wide5+reball5
                        print("\nTotal 5th Ball Run Is: ",Opp_Team_FifthBall_Run)

            elif run5 == "No Ball":

                    print("\nBall Is: ",run5)
                    print("Extra Run Is: ",Noball5, "No Ball Attend By: ",reball5)
                    
                    print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                    
                    Free_Run5=random.choice((0,1,2,3,4,6))
                    FreeHit5=Free_Run5

                    No_Reball_V= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                    if No_Reball_V == "":
                        print("\nFREE HIT!!! Hit By: ",FreeHit5)

                        Opp_Team_FifthBall_Run += Noball5+reball5+FreeHit5
                        print("\nTotal 5th Ball Run Is: ",Opp_Team_FifthBall_Run)
                
            elif run5 == "Out":
                    Opp_Team_FifthBall_Run += Out5
                    print("\nYou Are: ",run5)
                    print("\n5th Ball Out Run Consider As: ",Out5)

            elif fifth_ball == "":
                    print("\n5th Ball Run: ",run5)
                    Opp_Team_FifthBall_Run += run5
                    
                    
            else:
                    print("\nEnter The Correct Number")


    # -----------------------------SIXTH BALL STARTS FROM-------------------------------------------------------------------------

            run_choice6=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
            run6=run_choice6

            reball_run6=random.choice((0,1,2,3,4,6))
            reball6=reball_run6

            Noball6=1
            Wide6=1
            Out6=0

            Opp_Team_SixthBall_Run = 0
                
            sixth_ball=input("\nPress ( 'ENTER' ) To Deliver The Sixth Ball: ")

            if run6 == "Wide":
                    print("\nBall Is: ",run6)
                    print("Extra Run: ",Wide6)

                    Reball_VI=input("\nPress ( 'ENTER' ) Reball ENTER 6: ")

                    if Reball_VI == "":
                        print("\nWide Reball Run: ",reball6)
                        
                        Opp_Team_SixthBall_Run += Wide6+reball6
                        print("\nTotal 6th Ball Run Is: ",Opp_Team_SixthBall_Run)

            elif run6 == "No Ball":

                    print("\nBall Is: ",run6)
                    print("Extra Run Is: ",Noball6, "No Ball Attend By: ",reball6)
                    
                    print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                    
                    Free_Run6=random.choice((0,1,2,3,4,6))
                    FreeHit6=Free_Run6

                    No_Reball_VI= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                    if No_Reball_VI == "":
                        print("\nFREE HIT!!! Hit By: ",FreeHit6)

                        Opp_Team_SixthBall_Run += Noball6+reball6+FreeHit6
                        print("\nTotal 6th Ball Run Is: ",Opp_Team_SixthBall_Run)
                
            elif run6 == "Out":
                    Opp_Team_SixthBall_Run += Out6
                    print("\nYou Are: ",run6)
                    print("\n6th Ball Out Run Consider As: ",Out6)

            elif sixth_ball == "":
                    print("\n6th Ball Run: ",run6)
                    Opp_Team_SixthBall_Run += run6
                    
                    
            else:
                    print("\nEnter The Correct Number")

            Opponent_Total = Opp_Team_FirstBall_Run + Opp_Team_SecondBall_Run + Opp_Team_ThirdBall_Run + Opp_Team_FourthBall_Run + Opp_Team_FifthBall_Run + Opp_Team_SixthBall_Run

#----------------------------------------First Batting TOTAL-------------------------------------------------------------------------
        
            print (f"\n{OPPONENT_TEAMS} TOTAL SCORE: ",Opponent_Total)

#-----------------------------------A(OPPONENT) BOWLING------------------------------------------------------------------------------

            Beat=input(f"\t\nNOW ( {TEAMS} ) BATTING ... READY TO BEAT {OPPONENT_TEAMS} SCORE: ( -{Opponent_Total}- )\n\nIF YOU READY PRESS ( 'ENTER' ): ")

            first_ball=input("\nPress ( 'ENTER' ) To Deliver The First Ball: ")

            if run == "Wide":
                print("\nBall Is: ",run)
                print("Extra Run: ",Wide)

                Reball_I=input("\nPress ( 'ENTER' ) To Deliver The Reball: ")

                if Reball_I == "":
                    print("\nWide Reball Run: ",reball)
                    
                    My_Team_FirstBall_Run += Wide+reball
                    print("\nTotal 1st Ball Run Is: ",My_Team_FirstBall_Run)

            elif run == "No Ball":

                print("\nBall Is: ",run)
                print("Extra Run Is: ",Noball, "No Ball Attend By: ",reball)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run=random.choice((0,1,2,3,4,6))
                FreeHit=Free_Run

                No_Reball_I= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                if No_Reball_I == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit)

                    My_Team_FirstBall_Run += Noball+reball+FreeHit
                    print("\nTotal 1st Ball Run Is: ",My_Team_FirstBall_Run)
            
            elif run == "Out":
                print("\nYou Are: ",run)
                print("\n1st Ball Out Consider As: ",Out)

            elif first_ball == "":
                My_Team_FirstBall_Run += run
                print("\n1st Ball Run: ",run)
                
                
            else:
                print("\nEnter The Correct Number")

# -----------------------------SECOND BALL STARTS FROM-------------------------------------------------------------------------

            run_choice2=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
            run2=run_choice2

            reball_run2=random.choice((0,1,2,3,4,6))
            reball2=reball_run2

            Noball2=1
            Wide2=1
            Out2=0

            My_Team_SecondBall_Run=0
            
            second_ball=input("\nPress ( 'ENTER' ) To Deliver The Second Ball: ")

            if run2 == "Wide":
                print("\nBall Is: ",run2)
                print("Extra Run: ",Wide2)

                Reball_II=input("\nPress ( 'ENTER' ) Deliver The Reball: ")

                if Reball_II == "":
                    print("\nWide Reball Run: ",reball2)
                    
                    My_Team_SecondBall_Run += Wide2+reball2
                    print("\nTotal 2nd Ball Run Is: ",My_Team_SecondBall_Run)

            elif run2 == "No Ball":

                print("\nBall Is: ",run2)
                print("Extra Run Is: ",Noball2, "No Ball Attend By: ",reball2)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run2=random.choice((0,1,2,3,4,6))
                FreeHit2=Free_Run2

                No_Reball_II= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                if No_Reball_II == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit2)

                    My_Team_SecondBall_Run += Noball2+reball2+FreeHit2
                    print("\nTotal 2nd Ball Run Is: ",My_Team_SecondBall_Run)
            
            elif run2 == "Out":
                print("\nYou Are: ",run2)
                print("\n2nd Ball Out Run Consider As: ",Out2)

            elif second_ball == "":
                print("\n2nd Ball Run: ",run2)
                My_Team_SecondBall_Run += run2
                
                
            else:
                print("\nEnter The Correct Number")


# -----------------------------THIRD BALL STARTS FROM-------------------------------------------------------------------------

            run_choice3=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
            run3=run_choice3

            reball_run3=random.choice((0,1,2,3,4,6))
            reball3=reball_run3

            Noball3=1
            Wide3=1
            Out3=0

            My_Team_ThirdBall_Run=0
            
            third_ball=input("\nPress ( 'ENTER' ) To Deliver The Third Ball: ")

            if run3 == "Wide":
                print("\nBall Is: ",run3)
                print("Extra Run: ",Wide3)

                Reball_III=input("\nPress ( 'ENTER' ) Deliver The Reball: ")

                if Reball_III == "":
                    print("\nWide Reball Run: ",reball3)
                    
                    My_Team_ThirdBall_Run += Wide3+reball3
                    print("\nTotal 3rd Ball Run Is: ",My_Team_ThirdBall_Run)

            elif run3 == "No Ball":

                print("\nBall Is: ",run3)
                print("Extra Run Is: ",Noball3, "No Ball Attend By: ",reball3)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run3=random.choice((0,1,2,3,4,6))
                FreeHit3=Free_Run3

                No_Reball_III= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                if No_Reball_III == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit3)

                    My_Team_ThirdBall_Run += Noball3+reball3+FreeHit3
                    print("\nTotal 3rd Ball Run Is: ",My_Team_ThirdBall_Run)
            
            elif run3 == "Out":
                print("\nYou Are: ",run3)
                print("\n3rd Ball Out Run Consider As: ",Out3)

            elif third_ball == "":
                print("\n3rd Ball Run: ",run3)
                My_Team_ThirdBall_Run += run3
                
                
            else:
                print("\nEnter The Correct Number")

# -----------------------------FOURTH BALL STARTS FROM-------------------------------------------------------------------------

            run_choice4=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
            run4=run_choice4

            reball_run4=random.choice((0,1,2,3,4,6))
            reball4=reball_run4

            Noball4=1
            Wide4=1
            Out4=0

            My_Team_FourthBall_Run=0
            
            fourth_ball=input("\nPress ( 'ENTER' ) To Deliver The Fourth Ball: ")

            if run4 == "Wide":
                print("\nBall Is: ",run4)
                print("Extra Run: ",Wide4)

                Reball_IV=input("\nPress ( 'ENTER' ) Deliver The Reball: ")

                if Reball_IV == "":
                    print("\nWide Reball Run: ",reball4)
                    
                    My_Team_FourthBall_Run += Wide4+reball4
                    print("\nTotal 4rd Ball Run Is: ",My_Team_FourthBall_Run)

            elif run4 == "No Ball":

                print("\nBall Is: ",run4)
                print("Extra Run Is: ",Noball4, "No Ball Attend By: ",reball4)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run4=random.choice((0,1,2,3,4,6))
                FreeHit4=Free_Run4

                No_Reball_IV= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                if No_Reball_IV == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit4)

                    My_Team_FourthBall_Run += Noball4+reball4+FreeHit4
                    print("\nTotal 4th Ball Run Is: ",My_Team_FourthBall_Run)
            
            elif run4 == "Out":
                print("\nYou Are: ",run4)
                print("\n4th Ball Out Run Consider As: ",Out4)

            elif fourth_ball == "":
                print("\n4th Ball Run: ",run4)
                My_Team_FourthBall_Run += run4
                
                
            else:
                print("\nEnter The Correct Number")


# -----------------------------FIFTH BALL STARTS FROM-------------------------------------------------------------------------

            run_choice5=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
            run5=run_choice5

            reball_run5=random.choice((0,1,2,3,4,6))
            reball5=reball_run5

            Noball5=1
            Wide5=1
            Out5=0

            My_Team_FifthBall_Run=0
            
            fifth_ball=input("\nPress ( 'ENTER' ) To Deliver The Fifth Ball: ")

            if run5 == "Wide":
                print("\nBall Is: ",run5)
                print("Extra Run: ",Wide5)

                Reball_V=input("\nPress ( 'ENTER' ) To Deliver The Reball: ")

                if Reball_V == "":
                    print("\nWide Reball Run: ",reball5)
                    
                    My_Team_FifthBall_Run += Wide5+reball5
                    print("\nTotal 5th Ball Run Is: ",My_Team_FifthBall_Run)

            elif run5 == "No Ball":

                print("\nBall Is: ",run5)
                print("Extra Run Is: ",Noball5, "No Ball Attend By: ",reball5)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run5=random.choice((0,1,2,3,4,6))
                FreeHit5=Free_Run5

                No_Reball_V= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                if No_Reball_V == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit5)

                    My_Team_FifthBall_Run += Noball5+reball5+FreeHit5
                    print("\nTotal 5th Ball Run Is: ",My_Team_FifthBall_Run)
            
            elif run5 == "Out":
                print("\nYou Are: ",run5)
                print("\n5th Ball Out Run Consider As: ",Out5)

            elif fifth_ball == "":
                print("\n5th Ball Run: ",run5)
                My_Team_FifthBall_Run += run5
                
                
            else:
                print("\nEnter The Correct Number")


# -----------------------------SIXTH BALL STARTS FROM-------------------------------------------------------------------------

            run_choice6=random.choice((0,1,2,3,4,6,"Out","Wide","No Ball"))
            run6=run_choice6

            reball_run6=random.choice((0,1,2,3,4,6))
            reball6=reball_run6

            Noball6=1
            Wide6=1
            Out6=0

            My_Team_SixthBall_Run=0
            
            sixth_ball=input("\nPress ( 'ENTER' ) To Deliver The Sixth Ball: ")

            if run6 == "Wide":
                print("\nBall Is: ",run6)
                print("Extra Run: ",Wide6)

                Reball_VI=input("\nPress ( 'ENTER' ) Reball ENTER 6: ")

                if Reball_VI == "":
                    print("\nWide Reball Run: ",reball6)
                    
                    My_Team_SixthBall_Run += Wide6+reball6
                    print("\nTotal 6th Ball Run Is: ",My_Team_SixthBall_Run)

            elif run6 == "No Ball":

                print("\nBall Is: ",run6)
                print("Extra Run Is: ",Noball6, "No Ball Attend By: ",reball6)
                
                print("\n\tFREE HIT!!! FREE HIT!!! FREE HIT!!!")
                
                Free_Run6=random.choice((0,1,2,3,4,6))
                FreeHit6=Free_Run6

                No_Reball_VI= input("Press ( 'ENTER' ) to Bowl The FREE HIT BALL!!!: ")

                if No_Reball_VI == "":
                    print("\nFREE HIT!!! Hit By: ",FreeHit6)

                    My_Team_SixthBall_Run += Noball6+reball6+FreeHit6
                    print("\nTotal 6th Ball Run Is: ",My_Team_SixthBall_Run)
            
            elif run6 == "Out":
                print("\nYou Are: ",run6)
                print("\n6th Ball Out Run Consider As: ",Out6)

            elif sixth_ball == "":
                print("\n6th Ball Run: ",run6)
                My_Team_SixthBall_Run += run6
                
                
            else:
                print("\nEnter The Correct Number")

            MyTeam_Total = My_Team_FirstBall_Run + My_Team_SecondBall_Run + My_Team_ThirdBall_Run + My_Team_FourthBall_Run + My_Team_FifthBall_Run + My_Team_SixthBall_Run

#----------------------------------------First Batting TOTAL-------------------------------------------------------------------------
        
            print (f"\n{TEAMS} TOTAL SCORE: ",MyTeam_Total)


#--------------------------------------MATCH RESULT---------------------------------------------------------------------------------

        Opponent_Result = Opponent_Total - MyTeam_Total
        MyTeam_Result = MyTeam_Total - Opponent_Total

        if Opponent_Total > MyTeam_Total:
             
             print (f"\n\tMATCH WIN BY {OPPONENT_TEAMS} WITH ( {Opponent_Result} ) RUN DIFFRENCE !!!")
             break

        elif Opponent_Total < MyTeam_Total:
             
             print (f"\n\tMATCH WIN BY {TEAMS} WITH ( {MyTeam_Result} ) RUN DIFFRENCE !!!")
             break
        

    else:
          print("INPUT ERROR !!! ( ENTER VALID INPUT )")
        
##################################### - PROJECT ENDED HERE -  #######################################################################