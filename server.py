import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from method import method

from tornado.options import define, options
define("port", default=8001, help="run on the given port", type=int)

input_login={
    'number':'',
    'password':'',
}
input_getpassword={
    'number':'',
    'prblem':'',
    'answer':''
}
input_changepassword1={
    'number':'',
    'password':''
}
input_changepassword2={
    'number':'',
    'password':'',
    'problem':'',
    'answer':''
}
user={
    'number':''
}
checknumber={
    'student_number':'',
    'teacher_number':'',
    'fudaoyuan_number':'',
    'admain_number':''
}
here={
    'counselor':''
}
changestudentbehavior={
    'number':'',
    'behavior':''
}
changestudentinformation={
    'student_number':'',
    'student_name':'',
    'student_sex':'',
    'student_birsday':'',
    'student_identity':'',
    'student_departments':'',
    'student_job':'',
    'student_class_id':'',
    'student_location':'',
    'student_phone':'',
    'student_national':'',
    'student_school_time':'',
    'student_idnumber':'',
    'student_behavior':'',
    'student_liuji':'',
    'student_xiuxue':'',
    'student_temp':'',
    'student_class_num':''
}
score={
    'score_student_number':'',
    'score_course_id':'',
    'score_score':''
}
teacher={
    'teacher_id':'',
    'teacher_name':'',
    'teacher_sex':'',
    'teacher_phone':'',
    'teacher_title':'',
    'teacher_departments':'',
    'teacher_next':''
}
counselor={
    'counselor_id':'',
    'counselor_name':'',
    'counselor_sex':'',
    'counselor_phone':'',
    'counselor_departments':'',
    'counselor_next':''
}
remove={
    'student_school_time':'',
    'student_number':'',
    'teacher_id':'',
    'counselor_id':''
}
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        checknumber['student_number']='';
        checknumber['teacher_number'] = '';
        checknumber['fudaoyuan_number'] = '';
        checknumber['admain_number'] = '';
        user['number']='';
        self.render('login.html')

class lookpasswordHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('lookpassword.html')

class GetpasswordHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('getpassword.html')

class AdmainHandler(tornado.web.RequestHandler):
    def get(self):
        if checknumber['admain_number'] != '':
            self.render('admain.html')
        else:
            self.render('login.html')
class StudentHandler(tornado.web.RequestHandler):
    def get(self):
        if checknumber['student_number'] != '':
            self.render('student.html')
        else:
            self.render('login.html')
class TeacherHandler(tornado.web.RequestHandler):
    def get(self):
        if checknumber['teacher_number'] != '':
            self.render('teacher.html')
        else:
            self.render('login.html')
class FudaoyuanHandler(tornado.web.RequestHandler):
    def get(self):
        if checknumber['fudaoyuan_number'] != '':
            self.render('fudaoyuan.html')
        else:
            self.render('login.html')
class ChangepasswordHandler(tornado.web.RequestHandler):
    def get(self):
        if user['number'] != '':
            self.render('changepassword.html')
        else:
            self.render('login.html')
class SlinfoHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('studentlookmyinformation.html')
class SlmygraHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('studentlookmygrade.html')
class TlmyinfoHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('teacherlookmyinformation.html')
class LstugraHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('lookstudentgrade.html')
class FlmyinfoHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('fudaoyuanlookmyinformation.html')
class LstuinfoHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('lookstudentinformation.html')
class ChastubehaHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('changestudentbehavior.html')
class LclanatHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('lookclassnature.html')
class CstuinfoHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('changestudentinformation.html')
class CstugraHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('changestudentgrade.html')
class LteainfoHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('lookteacherinformation.html')
class LfdyinfoHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('lookfudaoyuaninformation.html')
class DaoruHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('daoru.html')
class PeopleHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('people.html')
class PageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('page.html')
###################################################################
#找回密码
class getpasswordHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        input_getpassword['number'] = self.get_argument('Number')
        input_getpassword['problem'] = self.get_argument('Problem')
        input_getpassword['answer'] = self.get_argument('Answer')
        result=md.getpassword_handler(input_getpassword)
        if result == 'false':
            self.write('false')
        else:
            self.write(result)
#修改密码 判断原始密码是否正确
class changepassword1Handler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        input_changepassword1['number'] = self.get_argument('Number')
        input_changepassword1['password'] = self.get_argument('Password0')
        result=md.changepassword1_handler(input_changepassword1)
        if result == 'false':
            self.write('false')
        else:
            self.write('true')
#修改用户密码 将新密码和验证问题更新到数据库中
class changepassword2Handler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        input_changepassword2['number'] = self.get_argument('Number')
        input_changepassword2['password'] = self.get_argument('Password1')
        input_changepassword2['problem'] = self.get_argument('Problem')
        input_changepassword2['answer'] = self.get_argument('Answer')
        result=md.changepassword2_handler(input_changepassword2)
        if result == 'false':
            self.write('false')
        else:
            self.write('true')
#登陆 判断用户名和密码是否正确
class loginHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        input_login['number'] = self.get_argument('number')
        input_login['password'] = self.get_argument('Password')
        user['number'] = input_login['number']
        if 't' in input_login['number']:
            checknumber['teacher_number']=input_login['number']
        elif 'f' in input_login['number']:
            checknumber['fudaoyuan_number']=input_login['number']
        elif 'a' in input_login['number']:
            checknumber['admain_number']=input_login['number']
        else:
            checknumber['student_number']=input_login['number']
        result=md.login_choose(input_login)
        self.write(result)
#学生查看自己信息
class stulmyinfoHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        user['number'] = self.get_argument('Number')
        result=md.slmy_info_search_sql(user)
        if result is not None:
            self.write(result)
        else:
            self.write('false')
#学生查看成绩
class stulmygraHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        user['number'] = self.get_argument('Number')
        results=md.slmygra_info_search_sql(user)
        if results is not None:
            result={
                'result':results
            }
            self.write(result)
        else:
            self.write('false')
#教师查看自己信息
class tealmyinfoHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        user['number'] = self.get_argument('Number')
        result=md.tlmy_info_search_sql(user)
        if result is not None:
            self.write(result)
        else:
            self.write('false')
#查看所有学生成绩
class lstugraHandler(tornado.web.RequestHandler):
    def get(self):
        results=md.lstugra_info_search_sql()
        if results is not None:
            result={
                'result':results
            }
            self.write(result)
        else:
            self.write('false')
#辅导员查看自己信息
class fdylmyinfoHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        user['number'] = self.get_argument('Number')
        result=md.flmy_info_search_sql(user)
        if result is not None:
            self.write(result)
        else:
            self.write('false')
#查看所有学生信息
class lstuinfoHandler(tornado.web.RequestHandler):
    def get(self):
        results=md.lstuinfo_info_search_sql()
        if results is not None:
            result={
                'result':results
            }
            self.write(result)
        else:
            self.write('false')
#辅导员查看所有学生部分信息，并修改个人行为
class lstusinfoHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        here['counselor_id'] = self.get_argument('counselor_id')
        results=md.lstusinfo_info_search_sql(here)
        if results is not None:
            result={
                'result':results
            }
            self.write(result)
        else:
            self.write('false')
#辅导员修改学生行为
class chastubehaHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        changestudentbehavior['number'] = self.get_argument('number')
        changestudentbehavior['behavior'] = self.get_argument('behavior')
        results=md.fchastube_info_search_sql(changestudentbehavior)
        if results == 'false':
            self.write('false')
        else:
            self.write('true')
#辅导员查看班级信息，并修改班级行为
class lookclassnatureHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        here['counselor_id'] = self.get_argument('counselor_id')
        results=md.lcn_info_search_sql(here)
        if results is not None:
            result={
                'result':results
            }
            self.write(result)
        else:
            self.write('false')
#辅导员修改班级行为
class chaclabehaHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        changestudentbehavior['number'] = self.get_argument('number')
        changestudentbehavior['behavior'] = self.get_argument('behavior')
        results=md.chaclabe_info_search_sql(changestudentbehavior)
        if results == 'false':
            self.write('false')
        else:
            self.write('true')
#取第一个学生信息
class gfsinfoHandler(tornado.web.RequestHandler):
    def get(self):
        results=md.gfsinfo_info_search_sql()
        if results is not None:
            self.write(results)
        else:
            self.write('false')
#取第一个tea信息
class gftinfoHandler(tornado.web.RequestHandler):
    def get(self):
        results=md.gftinfo_info_search_sql()
        if results is not None:
            self.write(results)
        else:
            self.write('false')
#取第一个fudaoyuan信息
class gffinfoHandler(tornado.web.RequestHandler):
    def get(self):
        results=md.gffinfo_info_search_sql()
        if results is not None:
            self.write(results)
        else:
            self.write('false')
#取chazhao学生信息
class glsinfoHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        changestudentinformation['student_number'] = self.get_argument('student_number')
        results=md.glsinfo_info_search_sql(changestudentinformation)
        if results is not None:
            self.write(results)
        else:
            self.write('false')
#取chazhao tea信息
class gltinfoHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        teacher['teacher_id'] = self.get_argument('teacher_id')
        results=md.gltinfo_info_search_sql(teacher)
        if results is not None:
            self.write(results)
        else:
            self.write('false')
#取chazhao fudaoyuan信息
class glfinfoHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        counselor['counselor_id'] = self.get_argument('counselor_id')
        results=md.glfinfo_info_search_sql(counselor)
        if results is not None:
            self.write(results)
        else:
            self.write('false')
#管理员编辑提交所有学生信息
class cstuinfoHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        changestudentinformation['student_number'] = self.get_argument('studentnumber')
        changestudentinformation['student_name'] = self.get_argument('studentname')
        changestudentinformation['student_sex'] = self.get_argument('studentsex')
        changestudentinformation['student_birsday'] = self.get_argument('studentbirsday')
        changestudentinformation['student_identity'] = self.get_argument('studentidentity')
        changestudentinformation['student_departments'] = self.get_argument('studentdepartments')
        changestudentinformation['student_job'] = self.get_argument('studentjob')
        changestudentinformation['student_class_id'] = self.get_argument('studentclass_id')
        changestudentinformation['student_location'] = self.get_argument('studentlocation')
        changestudentinformation['student_phone'] = self.get_argument('studentphone')
        changestudentinformation['student_national'] = self.get_argument('studentnational')
        changestudentinformation['student_school_time'] = self.get_argument('studentschool_time')
        changestudentinformation['student_idnumber'] = self.get_argument('studentidnumber')
        changestudentinformation['student_liuji'] = self.get_argument('studentliuji')
        changestudentinformation['student_xiuxue'] = self.get_argument('studentxiuxue')
        changestudentinformation['student_temp'] = self.get_argument('temp')
        print(changestudentinformation)
        results=md.chastuinfo_info_search_sql(changestudentinformation)
        if results == 'false':
            self.write('false')
        elif results == 'false0':
            self.write('false0')
        else:
            self.write('true')
#管理员编辑提交学生成绩
class cstugraHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        score['score_student_number'] = self.get_argument('studentnumber')
        score['score_course_id'] = self.get_argument('courseid')
        score['score_score'] = self.get_argument('score')
        results=md.cstugra_search_sql(score)
        if results == 'false':
            self.write('false')
        else:
            self.write('true')
#管理员查看教师信息
class lteainfoHandler(tornado.web.RequestHandler):
    def get(self):
        results=md.lteainfo_info_search_sql()
        if results is not None:
            result={
                'result':results
            }
            self.write(result)
        else:
            self.write('false')
#管理员修改教师信息
class cteainfoHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        teacher['teacher_id'] = self.get_argument('teacher_id')
        teacher['teacher_name'] = self.get_argument('teacher_name')
        teacher['teacher_sex'] = self.get_argument('teacher_sex')
        teacher['teacher_phone'] = self.get_argument('teacher_phone')
        teacher['teacher_title'] = self.get_argument('teacher_title')
        teacher['teacher_departments'] = self.get_argument('teacher_departments')
        teacher['teacher_next'] = self.get_argument('teacher_next')
        results=md.chateainfo_info_search_sql(teacher)
        if results == 'false':
            self.write('false')
        else:
            self.write('true')
#管理员查看辅导员信息
class lfdyinfoHandler(tornado.web.RequestHandler):
    def get(self):
        results=md.lfdyinfo_info_search_sql()
        if results is not None:
            result={
                'result':results
            }
            self.write(result)
        else:
            self.write('false')
#管理员修改辅导员信息
class cfdyinfoHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        counselor['counselor_id'] = self.get_argument('counselor_id')
        counselor['counselor_name'] = self.get_argument('counselor_name')
        counselor['counselor_sex'] = self.get_argument('counselor_sex')
        counselor['counselor_phone'] = self.get_argument('counselor_phone')
        counselor['counselor_departments'] = self.get_argument('counselor_departments')
        counselor['counselor_next'] = self.get_argument('counselor_next')
        results=md.chafdyinfo_info_search_sql(counselor)
        if results == 'false':
            self.write('false')
        else:
            self.write('true')
#导入数据
class daoruHandler(tornado.web.RequestHandler):
    def post(self):
        if not 'infile' in self.request.files:
            respon = {'issuccess':'no_file'}
            respon_json = tornado.escape.json_encode(respon)
            self.write('false')
        else:
            infile = self.request.files['infile'][0]
            end=md.daoru_handler(infile['filename'])
            print(end)
        if end is not None:
            if end=='true':
                self.write('true')
            else:
                self.write('false')
        else:
            self.write('true')
#生成登陆初始密码
class getloginHandler(tornado.web.RequestHandler):
    def get(self):
        results=md.getlogin_info_search_sql()
        if results is not None:
            if results=='true':
                self.write('true')
            elif results == 'false0':
                self.write('false0')
            elif results == 'false1':
                self.write('false1')
            elif results == 'false2':
                self.write('false2')
        else:
            self.write('true')
#删除毕业学生
class remove0Handler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        remove['student_school_time'] = self.get_argument('student_school_time')
        results = md.remove0_info_search_sql(remove)
        if results == 'false':
            self.write('false')
        elif results == 'false0':
            self.write('false0')
        else:
            self.write('true')
#删除学生
class remove1Handler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        remove['student_number'] = self.get_argument('student_number')
        results = md.remove1_info_search_sql(remove)
        if results == 'false':
            self.write('false')
        elif results == 'false0':
            self.write('false0')
        else:
            self.write('true')
#删除jiaoshi
class remove2Handler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        remove['teacher_id'] = self.get_argument('teacher_id')
        results = md.remove2_info_search_sql(remove)
        if results == 'false':
            self.write('false')
        elif results == 'false0':
            self.write('false0')
        else:
            self.write('true')
#删除fudaoyuan
class remove3Handler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        remove['counselor_id'] = self.get_argument('counselor_id')
        results = md.remove3_info_search_sql(remove)
        if results == 'false':
            self.write('false')
        elif results == 'false0':
            self.write('false0')
        else:
            self.write('true')
###################################################
if __name__ == '__main__':
    #数据库链接
    md=method()
    md.mysql_connect()

    #服务器建立
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=
        [
            (r'/', IndexHandler),
            ################################################
            (r'/login.html', LoginHandler),
            (r'/lookpassword.html', lookpasswordHandler),
            (r'/changepassword.html', ChangepasswordHandler),
            (r'/getpassword.html', GetpasswordHandler),
            ###############################################
            (r'/admain.html',AdmainHandler),
            (r'/student.html', StudentHandler),
            (r'/teacher.html', TeacherHandler),
            (r'/fudaoyuan.html', FudaoyuanHandler),
            #################################################
            (r'/studentlookmyinformation.html', SlinfoHandler),
            (r'/studentlookmygrade.html', SlmygraHandler),
            ##############################################
            (r'/teacherlookmyinformation.html', TlmyinfoHandler),
            ##################################################
            (r'/fudaoyuanlookmyinformation.html', FlmyinfoHandler),
            (r'/lookclassnature.html', LclanatHandler),
            (r'/changestudentbehavior.html', ChastubehaHandler),
            ##################################################
            (r'/lookteacherinformation.html', LteainfoHandler),
            (r'/lookstudentinformation.html', LstuinfoHandler),
            (r'/changestudentinformation.html', CstuinfoHandler),
            (r'/changestudentgrade.html', CstugraHandler),
            (r'/lookstudentgrade.html', LstugraHandler),
            (r'/lookfudaoyuaninformation.html', LfdyinfoHandler),
            (r'/daoru.html', DaoruHandler),
            (r'/people.html', PeopleHandler),
            (r'/page.html', PageHandler),
            ##################################################
            ####           get post请求     ###################
            ##################################################
            (r'/login',loginHandler),
            (r'/getpassword', getpasswordHandler),
            (r'/changepassword1', changepassword1Handler),
            (r'/changepassword2', changepassword2Handler),
            ###################################################
            (r'/studentlookmyinformation', stulmyinfoHandler),
            (r'/studentlookmygrade', stulmygraHandler),
            #################################################
            (r'/teacherlookmyinformation', tealmyinfoHandler),
            (r'/lookstudentgrade', lstugraHandler),
            #################################################
            (r'/fudaoyuanlookmyinformation', fdylmyinfoHandler),
            (r'/lookstudentinformation', lstuinfoHandler),
            (r'/lookstudentsomeinformation', lstusinfoHandler),
            (r'/changestudentbehavior', chastubehaHandler),
            (r'/lookclassnature', lookclassnatureHandler),
            (r'/changeclassbehavior', chaclabehaHandler),
            #################################################
            (r'/getfirststuinfo', gfsinfoHandler),
            (r'/getfirstteainfo', gftinfoHandler),
            (r'/getfirstfdyinfo', gffinfoHandler),
            (r'/getlookstudent', glsinfoHandler),
            (r'/getlookteacher', gltinfoHandler),
            (r'/getlookcounselor', glfinfoHandler),
            (r'/changestudentinformation', cstuinfoHandler),
            (r'/changestudentgrade', cstugraHandler),
            (r'/lookteacherinformation', lteainfoHandler),
            (r'/changeteacherinformation', cteainfoHandler),
            (r'/lookfudaoyuaninformation', lfdyinfoHandler),
            (r'/changefudaoyuaninformation', cfdyinfoHandler),
            (r'/daoru', daoruHandler),
            (r'/getlogin', getloginHandler),
            (r'/remove0', remove0Handler),
            (r'/remove1', remove1Handler),
            (r'/remove2', remove2Handler),
            (r'/remove3', remove3Handler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    md.mysql_close()