def r(progress_count, Progress_module_trailer, Do_not_Progress, exculdc):
    while True:
        print('Would you like to enter another set of data?')
        target = input("Enter 'y' for yes or 'q' to quit and view results:")
        if target == 'y':
            break
        elif target == 'q':
            

            for credit in progress_d.keys():
                print(credit,'Progress :',progress_d[credit])

            for credit in Progress_module_trailer_d.keys():
                print(credit,'Trailer',Progress_module_trailer_d[credit])

            for credit in Do_not_Progress_d.keys():
                print(credit,'do not progress',Do_not_Progress_d[credit])

            for credit in exculdc_d.keys():
                print(credit,'Exclude',exculdc_d[credit])
           

            return True



exculdc = 0
Do_not_Progress = 0
Progress_module_trailer = 0
progress_count = 0
one_tot = 0

exculdc_d={}
Do_not_Progress_d={}
Progress_module_trailer_d={}
progress_d={} 


while True:
        try:
            
            uni_number=input('input your university number')
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
                                progress_d[uni_number]=mPass,mdefer,mfail
                                print('Progress')
                                if r(progress_count, Progress_module_trailer, Do_not_Progress, exculdc):
                                    break

                            elif mPass == 100:
                                Progress_module_trailer = Progress_module_trailer + 1
                                Progress_module_trailer_d[uni_number]=mPass,mdefer,mfail
                                print('Progress(moduletrailer)')
                                if r(progress_count, Progress_module_trailer, Do_not_Progress, exculdc):
                                    break
                                

                            elif mfail >= 80:
                                exculdc = exculdc + 1
                                exculdc_d[uni_number]=mPass,mdefer,mfail
                                print("exculd")
                                if r(progress_count, Progress_module_trailer, Do_not_Progress, exculdc):
                                    break

                            else:
                                Do_not_Progress = Do_not_Progress + 1
                                exculdc_d[uni_number]=mPass,mdefer,mfail
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
