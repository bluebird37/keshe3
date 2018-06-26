from MysqlOrm import MysqlOrm
from MysqlSQL import SQL_general
import xlrd
import os.path
import pymysql
db=MysqlOrm()
SQL=SQL_general()

input={
    'number':'1',
    'name':'',
    'dept':'',
    'course':'',
    'diction':'',
    'email':'',
    'local':''
}

input_cancel={
    'teacher_number':'1',
    'student_number':'21',
    'teacher_week':'1',
    'reservation':'周一',
    'details':'1',
    'teacher_email':'',
    'student_email':'',
}
login={
    'number':'',
    'password':'',
    'options':''
}
removestudent={
    'class_id':'',
    'class_num':''
}
class method:
    ######################################
    """登陆
            查询用户是否存在
    """
    def login_choose(self, input_login):
        sql = SQL.login_search_sql(input_login)
        temp = input_login['number']
        result = db.execute(sql)
        db.commit()
        if result is not None:
            for row in result:
                if temp[0] == 'a':
                    if input_login['password'] == row['password']:
                        return '4'
                    else:
                        return '0'
                elif temp[0] == 'f':
                    if input_login['password'] == row['password']:
                        return '3'
                    else:
                        return '0'
                elif temp[0] == 't':
                    if input_login['password'] == row['password']:
                        return '2'
                    else:
                        return '0'
                else:
                    if input_login['password'] == row['password']:
                        return '1'
                    else:
                        return '0'
        elif result is None:
            return '0'
        else:
            return '0'
    ######################################
    """
        找回密码
    """
    def getpassword_handler(self,input_regsiter):
        sql=SQL.getpassword_search_sql(input_regsiter)
        results=db.execute(sql)
        if results is None:
            db.commit()
            return 'false'
        else:
            for result in results:
                password = result['password']
            db.commit()
            return password
    ######################################
    """修改密码
            判断原始密码密码是否正确
    """
    def changepassword1_handler(self,input_changepassword1):
        sql=SQL.changepassword1_search_sql(input_changepassword1)
        results=db.execute(sql)
        if results is None:
            db.commit()
            return 'false'
        else:
            for result in results:
                if result['password']==input_changepassword1['password']:
                    db.commit()
                    return 'true'
                else:
                    db.commit()
                    return 'false'
    ######################################
    """修改密码
            将新密码和验证问题更新到数据库中
    """
    def changepassword2_handler(self, input_changepassword2):
        sql = SQL.changepassword2_search_sql(input_changepassword2)
        db.execute_no_return(sql)
        db.commit()
    ######################################
    """学生查看自己信息
    """
    def slmy_info_search_sql(self,input):
        sql=SQL.slmy_info_search_sql(input)
        results=db.execute(sql)
        if results is not None:
            result=results[0]
        else :
            result=None
        db.commit()
        return result
    ######################################
    """学生查看自己成绩
    """
    def slmygra_info_search_sql(self, input):
        sql = SQL.slmygra_info_search_sql(input)
        results = db.execute(sql)
        db.commit()
        if results is not None:
            return results
        else:
            return None
    ######################################
    """teacher查看自己信息
    """
    def tlmy_info_search_sql(self, input):
        sql = SQL.tlmy_info_search_sql(input)
        results = db.execute(sql)
        if results is not None:
            result = results[0]
        else:
            result = None
        db.commit()
        return result
    ######################################
    """查看所有学生成绩
    """
    def lstugra_info_search_sql(self):
        sql = SQL.lstugra_info_search_sql()
        results = db.execute(sql)
        db.commit()
        if results is not None:
            return results
        else:
            return None
    ######################################
    """导员查看自己信息
    """
    def flmy_info_search_sql(self, input):
        sql = SQL.flmy_info_search_sql(input)
        results = db.execute(sql)
        if results is not None:
            result = results[0]
        else:
            result = None
        db.commit()
        return result
    ######################################
    """查看所有学生信息
    """
    def lstuinfo_info_search_sql(self):
        sql = SQL.lstuinfo_info_search_sql()
        results = db.execute(sql)
        db.commit()
        if results is not None:
            return results
        else:
            return None
    ######################################
    """辅导员查看所有学生部分信息，并修改个人行为
    """
    def lstusinfo_info_search_sql(self,input):
        sql = SQL.lstusinfo_info_search_sql(input)
        results = db.execute(sql)
        db.commit()
        if results is not None:
            return results
        else:
            return None
    ######################################
    """fudaoyuan添加学生行为
    """
    def fchastube_info_search_sql(self, input):
        sql = SQL.fchastube_info_search_sql(input)
        db.execute_no_return(sql)
        db.commit()
    ###################################
    """辅导员查看班级信息，并修改班级行为
        """
    def lcn_info_search_sql(self, input):
        sql = SQL.lcn_info_search_sql(input)
        results = db.execute(sql)
        db.commit()
        if results is not None:
            return results
        else:
            return None
    ####################################
    """辅导员修改班级行为
        """

    def chaclabe_info_search_sql(self, input):
        sql = SQL.chaclabe_info_search_sql(input)
        db.execute_no_return(sql)
        db.commit()
    # ############################
    """管理员编辑提交所有学生信息
    """
    def chastuinfo_info_search_sql(self, input):
        sql2_1 = SQL.chastuinfo2_1_info_search_sql(input)  ###返回新班级人
        result2_1 = db.execute(sql2_1)  ###返回新班级人数
        db.commit()
        print(result2_1)
        if result2_1 is not None:###判断新的班级是否存在
            sql0 = SQL.chastuinfo0_info_search_sql(input)
            sql1 = SQL.chastuinfo1_info_search_sql(input)
            db.execute_no_return(sql0)
            db.commit()
            db.execute_no_return(sql1)
            db.commit()
            ##########判断班级是否改了
            if input['student_temp'] != input['student_class_id']:
                sql2 = SQL.chastuinfo2_info_search_sql(input)  ###返回原班级人数
                result2 = db.execute(sql2)  ###返回原班级人数
                db.commit()
                resultcor = result2[0]###获取原班级人数
                resultcor2 = result2_1[0]###获取新班级人数
                input['student_class_num'] = str(int(resultcor['class_num']) - 1);
                print(input['student_class_num'])
                sql3 = SQL.chastuinfo3_info_search_sql(input)
                db.execute_no_return(sql3)###gengxin原班级人数
                db.commit()
                ###################
                input['student_class_num'] = str(int(resultcor2['class_num']) + 1);
                print(input['student_class_num'])
                sql3_1 = SQL.chastuinfo3_1_info_search_sql(input)
                db.execute_no_return(sql3_1)###gengxinxin班级人数
                db.commit()
        else:
            return 'false0'
    ################################
    """管理员编辑提交学生成绩
    """
    def cstugra_search_sql(self, input):
        sql = SQL.cstugra_search_sql(input)
        db.execute_no_return(sql)
        db.commit()
    ##################################
    # 管理员查看教师信息
    def lteainfo_info_search_sql(self):
        sql = SQL.lteainfo_info_search_sql()
        results = db.execute(sql)
        db.commit()
        if results is not None:
            return results
        else:
            return None
    ################################
    # 管理员修改教师信息
    def chateainfo_info_search_sql(self, input):
        sql0 = SQL.chatea0_info_info_search_sql(input)
        sql1 = SQL.chatea1_info_info_search_sql(input)
        db.execute_no_return(sql0)
        db.commit()
        db.execute_no_return(sql1)
        db.commit()
    #################################
    # 管理员查看辅导员信息
    def lfdyinfo_info_search_sql(self):
        sql = SQL.lfdyinfo_info_search_sql()
        results = db.execute(sql)
        db.commit()
        if results is not None:
            return results
        else:
            return None
    ################################
    # 管理员修改辅导员信息
    def chafdyinfo_info_search_sql(self, input):
        sql0 = SQL.chafdy0_info_info_search_sql(input)
        sql1 = SQL.chafdy1_info_info_search_sql(input)
        db.execute_no_return(sql0)
        db.commit()
        db.execute_no_return(sql1)
        db.commit()
    ####################################
    def movenewtable(self,resultget1):
        get = db.execute(
            """select * from oldstudent where oldstudent_number='%s'""" % (resultget1['student_number']))
        if get is None:
            db.execute_no_return(
                "insert into oldstudent values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                % (resultget1['student_number'], resultget1['student_name'], resultget1['student_sex'],
                   resultget1['student_birsday'], resultget1['student_identity'],
                   resultget1['student_departments'], resultget1['student_job'], resultget1['student_class_id'],
                   resultget1['student_location'], resultget1['student_phone'], resultget1['student_national'],
                   resultget1['student_school_time'], resultget1['student_idnumber'],
                   resultget1['student_behavior'], resultget1['student_liuji'], resultget1['student_xiuxue'],
                   resultget1['student_next']))
        else:
            db.execute_no_return("""update oldstudent set oldstudent_number='%s',
                                                                            oldstudent_name='%s',
                                                                            oldstudent_sex='%s',
                                                                            oldstudent_birsday='%s',
                                                                            oldstudent_identity='%s',
                                                                            oldstudent_departments='%s',
                                                                            oldstudent_job='%s',
                                                                            oldstudent_class_id='%s',
                                                                            oldstudent_location='%s',
                                                                            oldstudent_phone='%s',
                                                                            oldstudent_national='%s',
                                                                            oldstudent_school_time='%s',
                                                                            oldstudent_idnumber='%s',
                                                                            oldstudent_behavior='%s',
                                                                            dstudent_liuji='%s',
                                                                            oldstudent_xiuxue='%s',
                                                                            oldstudent_next='%s'
                                                      where oldstudent_number='%s'"""
                                 % (resultget1['student_number'], resultget1['student_name'],
                                    resultget1['student_sex'], resultget1['student_birsday'],
                                    resultget1['student_identity'], resultget1['student_departments'],
                                    resultget1['student_job'], resultget1['student_class_id'],
                                    resultget1['student_location'], resultget1['student_phone'],
                                    resultget1['student_national'], resultget1['student_school_time'],
                                    resultget1['student_idnumber'], resultget1['student_behavior'],
                                    resultget1['student_liuji'], resultget1['student_xiuxue'],
                                    resultget1['student_next'],resultget1['student_number']))

        ####################################
    def movenewtable2(self,resultget1):
        get = db.execute(
            """select * from oldteacher where oldteacher_id='%s'""" % (resultget1['teacher_id']))
        if get is None:
            db.execute_no_return(
                "insert into oldteacher values ('%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                % (resultget1['teacher_id'], resultget1['teacher_name'], resultget1['teacher_sex'],
                   resultget1['teacher_phone'], resultget1['teacher_title'],
                   resultget1['teacher_departments'], resultget1['teacher_next']))
        else:
            db.execute_no_return("""update oldteacher set oldteacher_id='%s',
                                                                                   oldteacher_name='%s',
                                                                                   oldteacher_sex='%s',
                                                                                   oldteacher_phone='%s',
                                                                                   oldteacher_title='%s',
                                                                                   oldteacher_departments='%s',
                                                                                   oldteacher_next='%s'
                                                             where oldteacher_id='%s'"""
                                 % (resultget1['teacher_id'], resultget1['teacher_name'], resultget1['teacher_sex'],
                                    resultget1['teacher_phone'], resultget1['teacher_title'],resultget1['teacher_departments'],resultget1['teacher_next'],resultget1['teacher_id']))
    #####################################
    def movenewtable3(self,resultget1):
        get = db.execute(
            """select * from oldcounselor where oldcounselor_id='%s'""" % (resultget1['counselor_id']))
        if get is None:
            db.execute_no_return(
                "insert into oldcounselor values ('%s', '%s', '%s', '%s', '%s', '%s')"
                % (resultget1['counselor_id'], resultget1['counselor_name'], resultget1['counselor_sex'],
                   resultget1['counselor_phone'], resultget1['counselor_departments'],
                   resultget1['counselor_next']))
        else:
            db.execute_no_return("""update oldcounselor set oldcounselor_id='%s',
                                                            oldcounselor_name='%s',
                                                            oldcounselor_sex='%s',
                                                            oldcounselor_phone='%s',
                                                            oldcounselor_departments='%s',
                                                            oldcounselor_next='%s'
                                                     where ooldcounselor_id='%s'"""
                                 % (resultget1['counselor_id'], resultget1['counselor_name'], resultget1['counselor_sex'],
                   resultget1['counselor_phone'], resultget1['counselor_departments'],
                   resultget1['counselor_next'],resultget1['counselor_id']))
    #####################################
    # 删除毕业学生
    def remove0_info_search_sql(self, input):
        sql = SQL.remove00_info_info_search_sql(input)#获取要移植的数据
        resultsget=db.execute(sql)
        print(resultsget)
        db.commit()
        if resultsget is not None:
            ###将信息移植到新表
            for resultget in resultsget:
                self.movenewtable(resultget)
            ###删除带有student_number的表
            sqlselect0 = SQL.removeselect0_info_info_search_sql(input)
            results0=db.execute(sqlselect0)
            db.commit()
            for result0 in results0:
                sqlremove02 = SQL.remove02_info_info_search_sql(result0)
                db.execute_no_return(sqlremove02)
                db.commit()
                sqlremove03 = SQL.remove03_info_info_search_sql(result0)
                db.execute_no_return(sqlremove03)
                db.commit()
            ###删除带有student_class_id的表
            sqlselect1 = SQL.removeselect1_info_info_search_sql(input)
            results1 = db.execute(sqlselect1)
            db.commit()
            for result1 in results1:
                sqlremove04 = SQL.remove04_info_info_search_sql(result1)
                db.execute_no_return(sqlremove04)
                db.commit()
                sqlremove05 = SQL.remove05_info_info_search_sql(result1)
                db.execute_no_return(sqlremove05)
                db.commit()
            ###删除student表
            sqlremove01 = SQL.remove01_info_info_search_sql(input)
            db.execute_no_return(sqlremove01)
            db.commit()
        else:
            return 'false0'
    ###############
    # 删除学生
    def remove1_info_search_sql(self, input):
        sql = SQL.remove11_info_info_search_sql(input)
        resultsget1 = db.execute(sql)
        print(resultsget1)
        db.commit()
        if resultsget1 is not None:

            ###将信息移植到新表
            for resultget1 in resultsget1:
                self.movenewtable(resultget1)
            ###删除带有student_number的表
            sqlremove07 = SQL.remove07_info_info_search_sql(input)
            db.execute_no_return(sqlremove07)
            db.commit()
            sqlremove08 = SQL.remove08_info_info_search_sql(input)
            db.execute_no_return(sqlremove08)
            db.commit()
            ###删除带有student_class_id的表
            sqlselect2 = SQL.removeselect2_info_info_search_sql(input)
            results2 = db.execute(sqlselect2)
            db.commit()
            result2=results2[0]
            ###班级表人数-1
            removestudent['class_id']=result2['student_class_id']
            sqlselectlnum = SQL.removeselectlnum_info_info_search_sql(removestudent)
            temps = db.execute(sqlselectlnum)
            db.commit()
            print(temps)
            temp=temps[0]
            removestudent['class_num']=str(int(temp['class_num']) - 1)
            print(removestudent)
            sqlremove10 = SQL.remove10_info_info_search_sql(removestudent)
            db.execute_no_return(sqlremove10)
            db.commit()
            ###删除student表
            sqlremove06 = SQL.remove06_info_info_search_sql(input)
            db.execute_no_return(sqlremove06)
            db.commit()
        else:
            return 'false0'
    #######
    #删除教师
    def remove2_info_search_sql(self, input):
        sql = SQL.remove22_info_info_search_sql(input)
        resultsget2 = db.execute(sql)
        db.commit()
        if resultsget2 is not None:
            ###将信息移植到新表
            for resultget2 in resultsget2:
                self.movenewtable2(resultget2)
            #删除教师表
            print("7889")
            sqlremovete0 = SQL.removete0_info_info_search_sql(input)
            db.execute_no_return(sqlremovete0)
            db.commit()
            # 设置课程表的教师为空
            sqlremovete1 = SQL.removete1_info_info_search_sql(input)
            db.execute_no_return(sqlremovete1)
            db.commit()
            # 删除denglu表
            sqlremovete2 = SQL.removete2_info_info_search_sql(input)
            db.execute_no_return(sqlremovete2)
            db.commit()
        else:
            return 'false0'
    #######
    # 删除辅导员
    def remove3_info_search_sql(self, input):
        sql = SQL.remove33_info_info_search_sql(input)
        resultsget3 = db.execute(sql)
        db.commit()
        if resultsget3 is not None:
            ###将信息移植到新表
            for resultget3 in resultsget3:
                self.movenewtable3(resultget3)
            # 删除辅导员表
            sqlremoveco0 = SQL.removeco0_info_info_search_sql(input)
            db.execute_no_return(sqlremoveco0)
            db.commit()
            # 设置class表的辅导员为空
            sqlremoveco1 = SQL.removeco1_info_info_search_sql(input)
            db.execute_no_return(sqlremoveco1)
            db.commit()
            # 删除denglu表
            sqlremoveco2 = SQL.removeco2_info_info_search_sql(input)
            db.execute_no_return(sqlremoveco2)
            db.commit()
        else:
            return 'false0'
    ###############################
    #######
    # 生成登陆初始密码
    def getlogin_info_search_sql(self):
        getlogins0 = db.execute("""select student_number,student_idnumber from student """)
        db.commit()
        if getlogins0 is not None:
            for getlogin0 in getlogins0:
                login['number']=getlogin0['student_number']
                login['password'] = getlogin0['student_idnumber'][12:]
                login['options'] = '0'
                print(login['password'])
                return0 = db.execute("select * from login where numberall='%s'" % (login['number']))
                db.commit()
                if return0 is None:
                    db.execute_no_return("insert into login (numberall,password,optionsall) values ('%s', '%s', '%s')"
                                         % (login['number'],login['password'],login['options']))
                    db.commit()
                else:
                    db.execute_no_return("""update login set password='%s',optionsall='%s' where numberall='%s'""" % (login['password'],login['options'],login['number']))
                    db.commit()
        getlogins1 = db.execute("""select teacher_id from teacher """)
        db.commit()
        if getlogins1 is not None:
            for getlogin1 in getlogins1:
                login['number'] = getlogin1['teacher_id']
                login['password'] = '123456'
                login['options'] = '1'
                print(login['password'])
                return1 = db.execute("select * from login where numberall='%s'" % (login['number']))
                db.commit()
                if return1 is None:
                    db.execute_no_return("insert into login (numberall,password,optionsall) values ('%s', '%s', '%s')"
                                         % (login['number'],login['password'],login['options']))
                    db.commit()
                else:
                    db.execute_no_return("""update login set password='%s',optionsall='%s' where numberall='%s'""" % (login['password'],login['options'],login['number']))
        getlogins2 = db.execute("""select counselor_id from counselor """)
        db.commit()
        if getlogins2 is not None:
            for getlogin2 in getlogins2:
                login['number'] = getlogin2['counselor_id']
                login['password'] = '123456'
                login['options'] = '2'
                print(login['password'])
                return2 = db.execute("select * from login where numberall='%s'" % (login['number']))
                db.commit()
                if return2 is None:
                    db.execute_no_return("insert into login (numberall,password,optionsall) values ('%s', '%s', '%s')"
                                         % (login['number'],login['password'],login['options']))
                    db.commit()
                else:
                    db.execute_no_return("""update login set password='%s',optionsall='%s' where numberall='%s'""" % (login['password'],login['options'],login['number']))
        if getlogins0 is None:
            return 'false0'
        if getlogins1 is None:
            return 'false1'
        if getlogins2 is None:
            return 'false2'
    ##############################
    # 取第一个学生信息
    def gfsinfo_info_search_sql(self):
        sql = SQL.gfsinfo_info_search_sql()
        results = db.execute(sql)
        db.commit()
        if results is not None:
            result=results[0]
            return result
        else:
            return None
    # 取第一个tea信息
    def gftinfo_info_search_sql(self):
        sql = SQL.gftinfo_info_search_sql()
        results = db.execute(sql)
        db.commit()
        if results is not None:
            result=results[0]
            return result
        else:
            return None
    # 取第一个fudaoyuan信息
    def gffinfo_info_search_sql(self):
        sql = SQL.gffinfo_info_search_sql()
        results = db.execute(sql)
        db.commit()
        if results is not None:
            result = results[0]
            return result
        else:
            return None
    # 取chazhao学生信息
    def glsinfo_info_search_sql(self,input):
        sql = SQL.glsinfo_info_search_sql(input)
        results = db.execute(sql)
        db.commit()
        if results is not None:
            result = results[0]
            return result
        else:
            return None
    # 取chazhao tea信息
    def gltinfo_info_search_sql(self,input):
        sql = SQL.gltinfo_info_search_sql(input)
        results = db.execute(sql)
        db.commit()
        if results is not None:
            result = results[0]
            return result
        else:
            return None

    # 取chazhao fudaoyuan信息
    def glfinfo_info_search_sql(self,input):
        sql = SQL.glfinfo_info_search_sql(input)
        results = db.execute(sql)
        db.commit()
        if results is not None:
            result = results[0]
            return result
        else:
            return None
    ###############################
    """导入数据
        将excel表导入数据库中
    """
    def daoru_handler(self, input_name):
        filename=input_name
        if 'class.xlsx' in filename:
            filename='E:\\keshe3\\static\\table\\class.xlsx'
        elif 'counselor.xlsx' in filename:
            filename='E:\\keshe3\\static\\table\\counselor.xlsx'
        elif 'course.xlsx' in filename:
            filename='E:\\keshe3\\static\\table\\course.xlsx'
        elif 'score.xlsx' in filename:
            filename='E:\\keshe3\\static\\table\\score.xlsx'
        elif 'student.xlsx' in filename:
            filename='E:\\keshe3\\static\\table\\student.xlsx'
        else:
            filename = 'E:\\keshe3\\static\\table\\teacher.xlsx'
        # 建立mysql连接
        print(filename)
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(0)
        values=[]
        for r in range(1, sheet.nrows):
            for j in range(0,sheet.ncols):
                ctype = sheet.cell(r,j).ctype  # 判断python读取的返回类型  0 --empty,1 --string, 2 --number(都是浮点), 3 --date, 4 --boolean, 5 --error
                no = sheet.cell(r,j).value  # 获取单元格的值
                if ctype == 2:
                    no = str(int(no))  # 将浮点转换成整数再转换成字符串
                values.append(no)
        print(values)
        if 'class.xlsx' in filename:
            for n1 in range(0, sheet.nrows - 1):
                result = db.execute("""select * from class where class_id='%s'""" % (values[8 * n1]))
                if result is None:
                    db.execute_no_return("insert into class values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                                         % (values[8 * n1], values[8 * n1 + 1], values[8 * n1 + 2], values[8 * n1 + 3],
                                            values[8 * n1 + 4], values[8 * n1 + 5], values[8 * n1 + 6], values[8 * n1 + 7]))
                else:
                    db.execute_no_return("""update class set class_id='%s',
                                                                class_departments='%s',
                                                                class_job='%s',
                                                                class_num='%s',
                                                                class_counselor_id='%s',
                                                                class_counselor_name='%s',
                                                                class_nature='%s',
                                                                class_next='%s' 
                              where class_id='%s'"""
                                         % (values[8 * n1], values[8 * n1 + 1], values[8 * n1 + 2], values[8 * n1 + 3],
                                            values[8 * n1 + 4], values[8 * n1 + 5], values[8 * n1 + 6],
                                            values[8 * n1 + 7], values[8 * n1]))
        elif 'counselor.xlsx' in filename:
            for n1 in range(0, sheet.nrows - 1):
                result = db.execute("""select * from counselor where counselor_id='%s'""" % (values[6 * n1]))
                if result is None:
                    db.execute_no_return("insert into counselor values ('%s', '%s', '%s', '%s', '%s', '%s')"
                                         % (values[6 * n1], values[6 * n1 + 1], values[6 * n1 + 2], values[6 * n1 + 3],
                                            values[6 * n1 + 4], values[6 * n1 + 5]))
                else:
                    db.execute_no_return("""update counselor set counselor_id='%s',
                                                                    counselor_name='%s',
                                                                    counselor_sex='%s',
                                                                    counselor_phone='%s',
                                                                    counselor_departments='%s',
                                                                    counselor_next='%s' 
                               where counselor_id='%s'"""
                                         % (values[6 * n1], values[6 * n1 + 1], values[6 * n1 + 2], values[6 * n1 + 3],
                                            values[6 * n1 + 4], values[6 * n1 + 5], values[6 * n1]))
        elif 'course.xlsx' in filename:
            for n1 in range(0, sheet.nrows - 1):
                result = db.execute(
                    """select * from course where (course_id='%s'and course_class_id='%s')""" % (
                        values[12 * n1], values[12 * n1 + 3]))
                if result is None:
                    db.execute_no_return(
                        "insert into course (course_id,course_name,course_nature,course_class_id,course_time,course_job,course_score,course_term,course_test_nature,course_teacher_id,course_teacher_name,course_next) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                        % (values[12 * n1], values[12 * n1 + 1], values[12 * n1 + 2], values[12 * n1 + 3],
                           values[12 * n1 + 4], values[12 * n1 + 5], values[12 * n1 + 6], values[12 * n1 + 7],
                           values[12 * n1 + 8], values[12 * n1 + 9], values[12 * n1 + 10], values[12 * n1 + 11]))
                else:
                    db.execute_no_return("""update course set course_id='%s',
                                                                course_name='%s',
                                                                course_nature='%s',
                                                                course_class_id='%s',
                                                                course_time='%s',
                                                                course_job='%s',
                                                                course_score='%s',
                                                                course_term='%s',
                                                                course_test_nature='%s',
                                                                course_teacher_id='%s',
                                                                course_teacher_name='%s',
                                                                course_next='%s'
                                where (course_id='%s'and course_class_id='%s')"""
                                         % (
                                             values[12 * n1], values[12 * n1 + 1], values[12 * n1 + 2], values[12 * n1 + 3],
                                             values[12 * n1 + 4], values[12 * n1 + 5], values[12 * n1 + 6],
                                             values[12 * n1 + 7],
                                             values[12 * n1 + 8], values[12 * n1 + 9], values[12 * n1 + 10],values[12 * n1 + 11],values[12 * n1], values[12 * n1 + 3]))
        elif 'score.xlsx' in filename:
            for n1 in range(0, sheet.nrows - 1):
                result = db.execute("""select * from score where (score_course_id='%s'and score_student_number='%s')""" % (
                    values[10 * n1], values[10 * n1 + 2]))
                if result is None:
                    db.execute_no_return(
                        "insert into score (score_course_id,score_course_name,score_student_number,score_student_name,score_score,score_class_id,score_term,score_course_nature,score_test_nature,score_sourse_next) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                        % (values[10 * n1], values[10 * n1 + 1], values[10 * n1 + 2], values[10 * n1 + 3],
                           values[10 * n1 + 4], values[10 * n1 + 5], values[10 * n1 + 6], values[10 * n1 + 7],
                           values[10 * n1 + 8], values[10 * n1 + 9]))
                else:
                    db.execute_no_return("""update score set score_course_id='%s',
                                                                score_course_name='%s',
                                                                score_student_number='%s',
                                                                score_student_name='%s',
                                                                score_score='%s',
                                                                score_class_id='%s',
                                                                score_term='%s',
                                                                score_course_nature='%s',
                                                                score_test_nature='%s',
                                                                score_sourse_next='%s' 
                                  where (score_course_id='%s' and score_student_number='%s')"""
                                         % (
                                             values[10 * n1], values[10 * n1 + 1], values[10 * n1 + 2], values[10 * n1 + 3],
                                             values[10 * n1 + 4], values[10 * n1 + 5], values[10 * n1 + 6],
                                             values[10 * n1 + 7],
                                             values[10 * n1 + 8], values[10 * n1 + 9], values[10 * n1],
                                             values[10 * n1 + 2]))
        elif 'student.xlsx' in filename:
            for n1 in range(0, sheet.nrows - 1):
                result = db.execute("""select * from student where student_number='%s'""" % (values[17 * n1]))
                if result is None:
                    db.execute_no_return(
                        "insert into student values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                        % (values[17 * n1], values[17 * n1 + 1], values[17 * n1 + 2], values[17 * n1 + 3],
                           values[17 * n1 + 4], values[17 * n1 + 5], values[17* n1 + 6], values[17 * n1 + 7]
                           , values[17 * n1 + 8], values[17 * n1 + 9], values[17 * n1 + 10],
                           values[17 * n1 + 11], values[17 * n1 + 12], values[17 * n1 + 13], values[17 * n1 + 14],values[17 * n1 + 15], values[17 * n1 + 16]))
                else:
                    db.execute_no_return("""update student set student_number='%s',
                                                        student_name='%s',
                                                        student_sex='%s',
                                                        student_birsday='%s',
                                                        student_identity='%s',
                                                        student_departments='%s',
                                                        student_job='%s',
                                                        student_class_id='%s',
                                                        student_location='%s',
                                                        student_phone='%s',
                                                        student_national='%s',
                                                        student_school_time='%s',
                                                        student_idnumber='%s',
                                                        student_behavior='%s',
                                                        student_liuji='%s',
                                                        student_xiuxue='%s',
                                                        student_next='%s'
                                  where student_number='%s'"""
                                         % (values[17 * n1], values[17 * n1 + 1], values[17 * n1 + 2], values[17 * n1 + 3],
                                            values[17 * n1 + 4], values[17 * n1 + 5], values[17 * n1 + 6], values[17 * n1 + 7]
                                            , values[17 * n1 + 8], values[17 * n1 + 9], values[17 * n1 + 10],
                                            values[17 * n1 + 11], values[17 * n1 + 12], values[17 * n1 + 13],
                                            values[17 * n1 + 14],values[17 * n1 + 15], values[17 * n1 + 16],values[17 * n1]))
        elif 'teacher.xlsx' in filename:
            for n1 in range(0, sheet.nrows - 1):
                result = db.execute("""select * from teacher where teacher_id='%s'""" % (values[7 * n1]))
                if result is None:
                    db.execute_no_return("insert into teacher values ('%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                                         % (values[7 * n1], values[7 * n1 + 1], values[7 * n1 + 2], values[7 * n1 + 3],
                                            values[7 * n1 + 4], values[7 * n1 + 5], values[7 * n1 + 6]))
                else:
                    db.execute_no_return("""update teacher set teacher_id='%s',
                                                        teacher_name='%s',
                                                        teacher_sex='%s',
                                                        teacher_phone='%s',
                                                        teacher_title='%s',
                                                        teacher_departments='%s',
                                                        teacher_next='%s'
                                  where teacher_id='%s'"""
                                         % (values[7 * n1], values[7 * n1 + 1], values[7 * n1 + 2], values[7 * n1 + 3],
                                            values[7 * n1 + 4], values[7 * n1 + 5], values[7 * n1 + 6], values[7 * n1]))

        db.commit()
    ######################################
    ######################################
    ######################################
    ######################################
    """
        数据库链接接口
    """
    def mysql_connect(self):
        db.connect()

    """
        数据库关闭接口
    """
    def mysql_close(self):
        db.close()

if __name__ == '__main__':
    #数据库链接
    db=MysqlOrm()
    SQL=SQL_general()
    md=method()
    db.connect()
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "static")
    # input_time['1_1']='1'
    result=md.teacher_reservation_concel_sql(input_cancel)