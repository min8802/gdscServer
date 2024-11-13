# from django.urls import path, re_path
from django.conf.urls import url, handler400, handler403, handler404, handler500
from app import views , web3Views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^newAccount/$', views.newAccount, name='newAccount'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^checkEmail/$', views.checkEmail, name='checkEmail'),
    url(r'^checkUser/$', views.checkUser, name='checkUser'),
    url(r'^checkOTPCode/$', views.checkOTPCode, name='checkOTPCode'),
    url(r'^checkOTPCode2/$', views.checkOTPCode2, name='checkOTPCode2'),
    url(r'^userSettingModiPW/$', views.userSettingModiPW, name='userSettingModiPW'),
    url(r'^userLoginDateUp/$', views.userLoginDateUp, name='userLoginDateUp'),
    url(r'^updateUserinfo/$', views.updateUserinfo, name='updateUserinfo'),
    url(r'^web3newAcc/$', views.web3newAcc, name='web3newAcc'),
    url(r'^newsinfo/$', views.newsinfo, name='newsinfo'),

    url(r'^SolutionRequest/$', views.SolutionRequest, name='SolutionRequest'),
    url(r'^SolutionIng/$', views.SolutionIng, name='SolutionIng'),
    url(r'^MySolution/$', views.MySolution, name='MySolution'),
    url(r'^solution1Upload/$', views.solution1Upload, name='solution1Upload'),
    url(r'^solution1UpImgDel/$', views.solution1UpImgDel, name='solution1UpImgDel'),
    url(r'^solution2Upload/$', views.solution2Upload, name='solution2Upload'),
    url(r'^solution2UpImgDel/$', views.solution2UpImgDel, name='solution2UpImgDel'),
    url(r'^solution3Upload/$', views.solution3Upload, name='solution3Upload'),
    url(r'^solution3UpImgDel/$', views.solution3UpImgDel, name='solution3UpImgDel'),
    url(r'^solution4Upload/$', views.solution4Upload, name='solution4Upload'),
    url(r'^solution4UpImgDel/$', views.solution4UpImgDel, name='solution4UpImgDel'),
    url(r'^solution5Upload/$', views.solution5Upload, name='solution5Upload'),
    url(r'^solution5UpImgDel/$', views.solution5UpImgDel, name='solution5UpImgDel'),
    url(r'^solution6Upload/$', views.solution6Upload, name='solution6Upload'),
    url(r'^solution6UpImgDel/$', views.solution6UpImgDel, name='solution6UpImgDel'),
    url(r'^userSendGDSC/$', views.userSendGDSC, name='userSendGDSC'),
    url(r'^ethTransfer/$', views.ethTransfer, name='ethTransfer'),
    url(r'^ethWithdraw/$', views.ethWithdraw, name='ethWithdraw'),
    url(r'^TtoClist/$', views.TtoClist, name='TtoClist'),
    url(r'^userEthWallet111/$', views.userEthWallet111, name='userEthWallet111'),
    url(r'^userEthWalletSave/$', views.userEthWalletSave, name='userEthWalletSave'),
    url(r'^userEthWalletList/$', views.userEthWalletList, name='userEthWalletList'),
    url(r'^addrcheck/$', views.addrcheck, name='addrcheck'),
    url(r'^TtoCsave/$', views.TtoCsave, name='TtoCsave'),
    url(r'^CtoTsave/$', views.CtoTsave, name='CtoTsave'),
    url(r'^userGDSCWalletSave/$', views.userGDSCWalletSave, name='userGDSCWalletSave'),
    url(r'^userGdscWalletList/$', views.userGdscWalletList, name='userGdscWalletList'),
    url(r'^gdscWithdraw/$', views.gdscWithdraw, name='gdscWithdraw'),
    url(r'^solutionPageDel/$', views.solutionPageDel, name='solutionPageDel'),
    url(r'^ethlookTime/$', views.ethlookTime, name='ethlookTime'),
    url(r'^TESDGDS/$', views.TESDGDS, name='TESDGDS'),
    url(r'^gdsclookTime/$', views.gdsclookTime, name='gdsclookTime'),
    url(r'^safenotifi/$', views.safenotifi, name='safenotifi'),
    url(r'^solutionnotifi/$', views.solutionnotifi, name='solutionnotifi'),
    url(r'^tokensava/$', views.tokensava, name='tokensava'),
    url(r'^bellset/$', views.bellset, name='bellset'),
    url(r'^bellsave/$', views.bellsave, name='bellsave'),



    url(r'^testWall/$', web3Views.testWall, name='testWall'),
    url(r'^testWall111/$', web3Views.testWall111, name='testWall111'),
    url(r'^test4028/$', web3Views.test4028, name='test4028'),
    url(r'^sendEthToUser/$', web3Views.sendEthToUser, name='sendEthToUser'),
    url(r'^testtest/$', web3Views.testtest, name='testtest'),


    # --------------------------------------------------------------------------------
    # 2022.07.19 - JS / 솔루션 이미지등록 수정
    url(r'^solutionUpload/$', views.solutionUpload, name='solutionUpload'),
    # 2022.07.21 JS - SMS 테스트
    url(r'^smsTest/$', views.smsTest, name='smsTest'),




    # url(r'^solutionPageDel/$', views.solutionPageDel, name='solutionPageDel'),
]
# + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    # re_path(r'^.*\.html', views.gentella_html, name='gentella'),
    # url(r'^', views.index, name='index'),
    # url('start', views.start, name='start'),
    # url(r'^start/$', views.start, name='start'),

    # path('signup', views.signup, name='signup'),
    # path('login', views.login, name='login'),
    # path('checkEmail', views.checkEmail, name='checkEmail'),
    # path('checkUser', views.checkUser, name='checkUser'),
    # path('checkOTPCode', views.checkOTPCode, name='checkOTPCode'),
    # path('checkOTPCode2', views.checkOTPCode2, name='checkOTPCode2'),
    # path('userSettingModiPW', views.userSettingModiPW, name='userSettingModiPW'),
    # path('userLoginDateUp', views.userLoginDateUp, name='userLoginDateUp'),
    # path('updateUserinfo', views.updateUserinfo, name='updateUserinfo'),
    # path('web3newAcc', views.web3newAcc, name='web3newAcc'),
    # path('newsinfo', views.newsinfo, name='newsinfo'),
    # path('newAccount', views.newAccount, name='newAccount'),
    # # path('newAccount', web3Views.newAccount, name='newAccount'),

    # path('SolutionRequest', views.SolutionRequest, name='SolutionRequest'),
    # path('SolutionIng', views.SolutionIng, name='SolutionIng'),
    # path('MySolution', views.MySolution, name='MySolution'),
    # path('solution1Upload', views.solution1Upload, name='solution1Upload'),
    # path('solution1UpImgDel', views.solution1UpImgDel, name='solution1UpImgDel'),
    # path('solution2Upload', views.solution2Upload, name='solution2Upload'),
    # path('solution2UpImgDel', views.solution2UpImgDel, name='solution2UpImgDel'),
    # path('solution3Upload', views.solution3Upload, name='solution3Upload'),
    # path('solution3UpImgDel', views.solution3UpImgDel, name='solution3UpImgDel'),
    # path('solution4Upload', views.solution4Upload, name='solution4Upload'),
    # # path('solution4UpImgDel', views.solution4UpImgDel, name='solution4UpImgDel'),
    # path('solution5Upload', views.solution5Upload, name='solution5Upload'),
    # path('solution5UpImgDel', views.solution5UpImgDel, name='solution5UpImgDel'),
    # path('solution6Upload', views.solution6Upload, name='solution6Upload'),
    # path('solution6UpImgDel', views.solution6UpImgDel, name='solution6UpImgDel'),
    # path('updateUserinfo', views.updateUserinfo, name='updateUserinfo'),
    # path('solutionPageDel', views.solutionPageDel, name='solutionPageDel'),
