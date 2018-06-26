# encoding:utf-8
class SQL_general:
    def __init__(self):
        pass
################################
    """登陆
        查询用户是否存在：
    """
    def login_search_sql(self, input):
        sql = """select * from login where numberall='%s'""" % (input['number'])
        return sql
################################
    """找回密码
    """
    def getpassword_search_sql(self, input):
        sql = """select password from login where (numberall='%s' and problem='%s' and answer='%s')""" % (
        input['number'], input['problem'], input['answer'])
        return sql
################################
    """修改密码
            判断原始密码密码是否正确
    """
    def changepassword1_search_sql(self, input):
        sql = """select password from login where numberall='%s'""" % (input['number'])
        return sql
################################
    """修改密码
         将新密码和验证问题更新到数据库中
    """
    def changepassword2_search_sql(self, input):
        sql = """update login set numberall='%s',password='%s',problem='%s',answer='%s' where numberall='%s'""" % (
            input['number'],input['password'],input['problem'],input['answer'],input['number'])
        return sql
###############################
    """学生查看自己信息
    """
    def slmy_info_search_sql(self, input):
        sql = """select student.student_number,student.student_name,student.student_sex,student.student_birsday,student.student_identity,student.student_departments,student.student_job,student.student_class_id,student.student_location,student.student_phone,student.student_national,student.student_school_time,student.student_idnumber,student.student_behavior,class.class_nature from student,class where (student.student_number='%s' and student.student_class_id=class.class_id)""" % (input['number'])
        return sql
###############################
    """学生查看自己成绩
    """
    def slmygra_info_search_sql(self, input):
        sql = """select course.course_id,course.course_name,score.score_score,course.course_term,course.course_time,course.course_score,course.course_teacher_name,course.course_nature,course.course_test_nature from course,score where (score.score_student_number='%s' and score.score_course_id=course.course_id and score.score_class_id=course.course_class_id)""" % (input['number'])
        return sql
########################################
    """teacher查看自己信息
    """
    def tlmy_info_search_sql(self, input):
        sql = """select * from teacher where (teacher_id='%s')""" % (input['number'])
        return sql
##########################################
    """查看所有学生成绩
    """
    def lstugra_info_search_sql(self):
        sql = "select score.score_student_number,score.score_student_name,score.score_course_id,score.score_course_name,score.score_score,score.score_class_id,course.course_teacher_name,score.score_term,score.score_course_nature,score.score_test_nature from course,score where (score.score_course_id=course.course_id and score.score_class_id=course.course_class_id)"
        return sql
########################################
    """导员查看自己信息
    """
    def flmy_info_search_sql(self, input):
        sql = """select * from counselor where (counselor_id='%s')""" % (input['number'])
        return sql
##########################################
    """查看所有学生信息
    """
    def lstuinfo_info_search_sql(self):
        sql = "select * from student "
        return sql
##########################################
    """辅导员查看所有学生部分信息，并修改个人行为
    """
    def lstusinfo_info_search_sql(self,input):
        sql = """select student.student_number,student.student_name,student.student_sex,student.student_departments,student.student_job,student.student_class_id,student.student_phone,student.student_behavior from student,class,counselor where (student.student_class_id=class.class_id and class.class_counselor_id=counselor.counselor_id and counselor.counselor_id='%s')""" % (
                input['counselor_id'])
        return sql
##########################################
    """fudaoyuan添加学生行为
    """
    def fchastube_info_search_sql(self,input):
        sql="""update student set student_behavior='%s' where student_number='%s'""" % (
                input['behavior'],input['number'])
        return sql
###########################################
    """辅导员查看班级信息，并修改班级行为
        """
    def lcn_info_search_sql(self, input):
        sql = """select class_id,class_departments,class_job,class_num,class_counselor_name,class_nature from class where (class_counselor_id='%s')""" % (input['counselor_id'])
        return sql
###########################################
    """辅导员修改班级行为
        """
    def chaclabe_info_search_sql(self, input):
        sql = """update class set class_nature='%s' where class_id='%s'""" % (
            input['behavior'], input['number'])
        return sql
#############################################
    """管理员编辑提交所有学生信息
        """
    def chastuinfo0_info_search_sql(self, input):
        sql = """update student set student_name='%s',student_sex='%s',student_birsday='%s',student_identity='%s',student_departments='%s',student_job='%s',student_class_id='%s',student_location='%s',student_phone='%s',student_national='%s',student_school_time='%s',student_idnumber='%s',student_liuji='%s',student_xiuxue='%s' where student_number='%s'""" % (
            input['student_name'],input['student_sex'],input['student_birsday'],input['student_identity'],input['student_departments'],input['student_job'],input['student_class_id'],input['student_location'],input['student_phone'],input['student_national'],input['student_school_time'],input['student_idnumber'],input['student_liuji'],input['student_xiuxue'], input['student_number'])
        return sql
    ##########修改对应的其他表的信息
    def chastuinfo1_info_search_sql(self, input):
        sql = """update score set score_student_name='%s',score_class_id='%s' where score_student_number='%s'""" % (
            input['student_name'],input['student_class_id'],input['student_number'])
        return sql
    ###返回原班级人数
    def chastuinfo2_info_search_sql(self, input):
        sql = """select class_num from class where class_id='%s'""" % (
            input['student_temp'])
        return sql
    ###返回修改后班级人数
    def chastuinfo2_1_info_search_sql(self, input):
        sql = """select class_num from class where class_id='%s'""" % (
            input['student_class_id'])
        return sql
    #########修改原班级人数
    def chastuinfo3_info_search_sql(self, input):
        sql = """update class set class_num='%s' where class_id='%s'""" % (
            input['student_class_num'],input['student_temp'])
        return sql
    #########修改新班级人数
    def chastuinfo3_1_info_search_sql(self, input):
        sql = """update class set class_num='%s' where class_id='%s'""" % (
            input['student_class_num'],input['student_class_id'])
        return sql
###########################################
    """管理员编辑提交学生成绩
    """
    def cstugra_search_sql(self, input):
        sql = """update score set score_score='%s' where (score_student_number='%s' and score_course_id='%s')""" % (
            input['score_score'],input['score_student_number'],input['score_course_id'])
        return sql
#############################################
    # 管理员查看教师信息
    def lteainfo_info_search_sql(self):
        sql = "select * from teacher "
        return sql
################################
    # 管理员修改教师信息
    def chatea0_info_info_search_sql(self, input):
        sql = """update teacher set teacher_name='%s',teacher_sex='%s',teacher_phone='%s',teacher_title='%s',teacher_departments='%s',teacher_next='%s' where teacher_id='%s'""" % (
            input['teacher_name'],input['teacher_sex'],input['teacher_phone'],input['teacher_title'],input['teacher_departments'],input['teacher_next'],input['teacher_id'])
        return sql
    def chatea1_info_info_search_sql(self, input):
        sql = """update course set course_teacher_name='%s' where course_teacher_id='%s'""" % (
            input['teacher_name'],input['teacher_id'])
        return sql
##########################################
    # 管理员查看辅导员信息
    def lfdyinfo_info_search_sql(self):
        sql = "select * from counselor "
        return sql
################################
    # 管理员修改辅导员信息
    def chafdy0_info_info_search_sql(self, input):
        sql = """update counselor set counselor_name='%s',counselor_sex='%s',counselor_phone='%s',counselor_departments='%s',counselor_next='%s' where counselor_id='%s'""" % (
            input['counselor_name'], input['counselor_sex'], input['counselor_phone'],
            input['counselor_departments'], input['counselor_next'], input['counselor_id'])
        return sql
    def chafdy1_info_info_search_sql(self, input):
        sql = """update class set class_counselor_name='%s'where class_counselor_id='%s'""" % (
            input['counselor_name'], input['counselor_id'])
        return sql
####################################
    # 删除毕业学生
    def remove00_info_info_search_sql(self, input):
        sql = """select * from student where student_school_time='%s'""" % (
            input['student_school_time'])
        return sql
    #############
    #删除学生表
    def remove01_info_info_search_sql(self, input):
        sql = """delete from student where student_school_time='%s'""" % (
            input['student_school_time'])
        return sql
    # 移植学生信息
    def removeselectmove_info_info_search_sql(self, input):
        sql = """delete from student where student_school_time='%s'""" % (
            input['student_school_time'])
        return sql
    #获取学生id
    def removeselect0_info_info_search_sql(self, input):
        sql = """select student_number from student where student_school_time='%s'""" % (
            input['student_school_time'])
        return sql
    # 获取学生class_id
    def removeselect1_info_info_search_sql(self, input):
        sql = """select student_class_id from student where student_school_time='%s'""" % (
            input['student_school_time'])
        return sql
    ############
    # 删除分数表
    def remove02_info_info_search_sql(self, input):
        sql = """delete from score where (score_student_number='%s')""" % (
            input['student_number'])
        return sql
    # 删除denglu表
    def remove03_info_info_search_sql(self, input):
        sql = """delete from login where (login.numberall='%s')""" % (input['student_number'])
        return sql
    # 删除course表
    def remove04_info_info_search_sql(self, input):
        sql = """delete from course where (course_class_id='%s')""" % (input['student_class_id'])
        return sql
    # 删除class表
    def remove05_info_info_search_sql(self, input):
        sql = """delete from class where (class_id='%s')""" % (input['student_class_id'])
        return sql
####################################
    # 查找学生是否存在
    def remove11_info_info_search_sql(self, input):
        sql = """select * from student where student_number='%s'""" % (
            input['student_number'])
        return sql
    #############
    #删除学生表
    def remove06_info_info_search_sql(self, input):
        sql = """delete from student where student_number='%s'""" % (
            input['student_number'])
        return sql
    # 获取学生class_id
    def removeselect2_info_info_search_sql(self, input):
        sql = """select student_class_id from student where student_number='%s'""" % (
            input['student_number'])
        return sql
    ############
    # 删除分数表
    def remove07_info_info_search_sql(self, input):
        sql = """delete from score where (score_student_number='%s')""" % (
            input['student_number'])
        return sql
    # 删除denglu表
    def remove08_info_info_search_sql(self, input):
        sql = """delete from login where (login.numberall='%s')""" % (input['student_number'])
        return sql
    #查被删除学生班级人数
    def removeselectlnum_info_info_search_sql(self, input):
        sql = """select class_num from class where (class_id='%s')""" % (input['class_id'])
        return sql
    # class表人数-1
    def remove10_info_info_search_sql(self, input):
        sql = """update class set class_num='%s' where (class_id='%s')""" % (input['class_num'],input['class_id'])
        return sql
######################
    #查找教师信息是否存在
    def remove22_info_info_search_sql(self, input):
        sql = """select * from teacher where teacher_id='%s'""" % (input['teacher_id'])
        return sql
        #############
        # 删除教师表
    def removete0_info_info_search_sql(self, input):
        sql = """delete from teacher where teacher_id='%s'""" % (
            input['teacher_id'])
        return sql
        # 设置课程表的教师为空
    def removete1_info_info_search_sql(self, input):
        sql = """update course set course_teacher_id='',course_teacher_name='' where course_teacher_id='%s'""" % (
            input['teacher_id'])
        return sql
    # 删除denglu表
    def removete2_info_info_search_sql(self, input):
        sql = """delete from login where (login.numberall='%s')""" % (input['teacher_id'])
        return sql
#######################
    # 查找辅导员信息是否存在
    def remove33_info_info_search_sql(self, input):
        sql = """select * from counselor where counselor_id='%s'""" % (input['counselor_id'])
        return sql
    #############
    # 删除辅导员表
    def removeco0_info_info_search_sql(self, input):
        sql = """delete from counselor where counselor_id='%s'""" % (
            input['counselor_id'])
        return sql
    # 设置class表的辅导员为空
    def removeco1_info_info_search_sql(self, input):
        sql = """update class set class_counselor_id='',class_counselor_name='' where class_counselor_id='%s'""" % (
            input['counselor_id'])
        return sql
    # 删除denglu表
    def removeco2_info_info_search_sql(self, input):
        sql = """delete from login where (login.numberall='%s')""" % (input['counselor_id'])
        return sql
    # # 取第一个学生信息
    def gfsinfo_info_search_sql(self):
        sql="select * from student"
        return sql;
    # 取第一个tea信息
    def gftinfo_info_search_sql(self):
        sql="select * from teacher"
        return sql;
    def gffinfo_info_search_sql(self):
        sql="select * from counselor"
        return sql;
    # # 取chaozhao学生信息
    def glsinfo_info_search_sql(self,input):
        sql = """select * from student where student_number='%s'""" % (input['student_number'])
        return sql;

    # 取chazhao tea信息
    def gltinfo_info_search_sql(self,input):
        sql = """select * from teacher where teacher_id='%s'""" % (input['teacher_id'])
        return sql;
    # 取chazhao fudaoyuan信息
    def glfinfo_info_search_sql(self,input):
        sql = """select * from counselor where counselor_id='%s'""" % (input['counselor_id'])
        return sql;