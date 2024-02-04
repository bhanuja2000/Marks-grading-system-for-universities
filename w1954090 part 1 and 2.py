def r(progress_count, Progress_module_trailer, Do_not_Progress, exculdc):
    while True:
        print('Would you like to enter another set of data?')
        target = input("Enter 'y' for yes or 'q' to quit and view results:")
        if target == 'y':
            break
        elif target == 'q':
            print('Histogram')
            print('Progress', progress_count, ":", progress_count * ('*'))
            print('Trailer', Progress_module_trailer, ":", Progress_module_trailer * ('*'))
            print("Retriever", Do_not_Progress, ":", Do_not_Progress * ('*'))
            print('Excluded', exculdc, ":", exculdc * ('*'))
            outcome_t=progress_count+Progress_module_trailer+Do_not_Progress+exculdc
            print(outcome_t,'outcomes in total') 

            for credit in progress_count_list:
                print('Progress : '+str(credit)[1:len(str(credit))-1])

            for credit in Progress_module_trailer_list:
                print('Trailer : '+str(credit)[1:len(str(credit))-1])

            for credit in Do_not_Progress_list:
                print('Do not Progress : '+str(credit)[1:len(str(credit))-1])

            for credit in exculdc_list:
                print('Exclude : '+str(credit)[1:len(str(credit))-1])
               

            return True



exculdc = 0
Do_not_Progress = 0
Progress_module_trailer = 0
progress_count = 0
one_tot = 0

exculdc_list = []
Do_not_Progress_list = []
Progress_module_trailer_list = []
progress_count_list = []


while True:
        try:
            

            mPass = int(input('Please enter your credits at pass:'))
            if mPass <= 120 and mPass % 20 == 0 and mPass >= 0:
                mdefer = int(input('Please enter your credit at defer:'))
                if mdefer <= 120 and mdefer % 20 == 0 and mdefer >= 0:
                    mfail = int(input('Please enter your credit at fail:'))
                    if mfail <= 120 and mfail % 20 == 0 and mfail >= 0:
                        one_tot = mPass + mdefer + mfail
                        if one_tot==120 and one_tot > 0:
                            if mPass == 120:
                                progress_count = progress_count + 1
                                progress_count_list.append([mPass,mdefer,mfail])
                                print('Progress')
                                if r(progress_count, Progress_module_trailer, Do_not_Progress, exculdc):
                                    break

                            elif mPass == 100:
                                Progress_module_trailer = Progress_module_trailer + 1
                                Progress_module_trailer_list.append([mPass,mdefer,mfail])
                                print('Progress(moduletrailer)')
                                if r(progress_count, Progress_module_trailer, Do_not_Progress, exculdc):
                                    break
                                

                            elif mfail >= 80:
                                exculdc = exculdc + 1
                                exculdc_list.append([mPass,mdefer,mfail])
                                print("exculd")
                                if r(progress_count, Progress_module_trailer, Do_not_Progress, exculdc):
                                    break

                            else:
                                Do_not_Progress = Do_not_Progress + 1
                                Do_not_Progress_list.append([mPass,mdefer,mfail])
                                print('Module retriever')
                                if r(progress_count, Progress_module_trailer, Do_not_Progress, exculdc):
                                    break
                        else:
                            print('total incorrect')
                    else:
                        print('out of range')
                else:
                    print('out of range')
            else:
                print('out of range')
        except:
            print('integer required')
