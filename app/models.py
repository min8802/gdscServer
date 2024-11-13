from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import UserManager
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# 여기는 GDSC App models입니다.

class SignUp(AbstractUser):
    name = models.CharField(max_length=150)                                                          # 회원 이름 (성)
    password = models.CharField(max_length=250)                                                      # 비밀번호
    phone = models.CharField(max_length=255, blank=True, null=True)                                  # 핸드폰 번호
    email = models.CharField(max_length=255, blank=True, null=True)                                  # 이메일
    ethAddr = models.CharField(max_length=255, blank=True, null=True)                                # 이더리움 주소
    otpCheck = models.CharField(max_length=250, blank=True, null=True, default = "0")                # otp 체크
    otpCode = models.CharField(max_length=255, blank=True, null=True)                                # otp 코드
    GDSTamount = models.CharField(max_length=255, blank=True, null=True, default = "0")              # 보유 중인 GDST
    GDSCamount = models.CharField(max_length=255, blank=True, null=True, default = "0")              # 보유 중인 GDST
    ethValue = models.CharField(max_length=255, blank=True, null=True, default = "0")                # 보유 중인 ETH
    tempSoluImg1 = models.CharField(max_length=255, blank=True, null=True)                           # 솔루션 이미지 1
    tempSoluImg2 = models.CharField(max_length=255, blank=True, null=True)                           # 솔루션 이미지 2
    tempSoluImg3 = models.CharField(max_length=255, blank=True, null=True)                           # 솔루션 이미지 3
    tempSoluImg4 = models.CharField(max_length=255, blank=True, null=True)                           # 솔루션 이미지 4
    tempSoluImg5 = models.CharField(max_length=255, blank=True, null=True)                           # 솔루션 이미지 5
    tempSoluImg6 = models.CharField(max_length=255, blank=True, null=True)                           # 솔루션 이미지 6
    ImgCount = models.IntegerField(blank=True, default = 0)                                          # IMG갯수
    walletMakeTime = models.CharField(max_length=255, blank=True, null=True)     # 유저의 지갑 생성 일자
    walletActive = models.CharField(max_length=255, blank=True, null=True)                           
    PushToken = models.CharField(max_length=255, blank=True, null=True)
    solutionPushStatus = models.CharField(max_length=255, blank=True, null=True, default = "1")
    safePushStatus = models.CharField(max_length=255, blank=True, null=True, default = "1")

    #핸드폰 인증
    DI = models.CharField(blank=True, max_length=255, null=True)
    CI = models.CharField(blank=True, max_length=255, null=True)
    CP_CD = models.CharField(max_length=30, blank=True, null=True)
    TX_SEQ_NO = models.CharField(max_length=30, blank=True, null=True)
    RSLT_CD = models.CharField(max_length=5, blank=True, null=True)
    TEL_COM_CD = models.CharField(max_length=3, blank=True, null=True)

class SafeNews(models.Model):
    newsRegisDate = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True) # 뉴스 등록일
    newsClass = models.CharField(max_length=255, blank=True, null=True)                             # 뉴스 종류 (0=건축법규, 1=건축기법, 2=재해예방가이드)
    newsTitle = models.CharField(max_length=255, blank=True, null=True)                             # 뉴스 제목
    newsContent = models.TextField(max_length=1000, blank=True, null=True)                          # 뉴스 내용
    newsStatus = models.CharField(max_length=255, blank=True, null=True, default = "0")             # 뉴스 상태값 (0=활성화, 1=비활성화 (앱에서 보이면 안됨))
    newsImg = models.CharField(max_length=255, blank=True, null=True)                               # 재해예방 가이드 일때, 들어가는 사진

class SolutionList(models.Model):
    soluRegisDate = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True) # 솔루션 등록 일자
    soluAnswerDate = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)# 솔루션 답변 일자
    buildingType = models.CharField(max_length=255, blank=True, null=True)                          # 건물 종류 (0=아파트, 1=빌라, 2=오피스텔, 3=전원주택, 4=상가주택, 5=한옥주택, 6=원룸, 7=투룸, 8=사무실, 9=상가, 10=기타 값 텍스트)
    paidGDST = models.CharField(max_length=255, blank=True, null=True)                              # 지불된 GDST 수량
    userEmail = models.CharField(max_length=255, blank=True, null=True)                             # 유저 이메일
    userName = models.CharField(max_length=150, blank=True, null=True)                              # 유저 이름 (성명)
    userphone = models.CharField(max_length=255, blank=True, null=True)                             # 유저 전화번호
    soluStatus = models.CharField(max_length=255, blank=True, null=True, default = "0")             # 솔루션 상태값 (0=활성화, 1=비활성화)
    solutionAnswer = models.TextField(max_length=1000, blank=True, null=True)                       # 솔루션 답변
    SoluImg1 = models.CharField(max_length=255, blank=True, null=True)                              # 솔루션 이미지 1
    SoluImg2 = models.CharField(max_length=255, blank=True, null=True)                              # 솔루션 이미지 2
    SoluImg3 = models.CharField(max_length=255, blank=True, null=True)                              # 솔루션 이미지 3
    SoluImg4 = models.CharField(max_length=255, blank=True, null=True)                              # 솔루션 이미지 4
    SoluImg5 = models.CharField(max_length=255, blank=True, null=True)                              # 솔루션 이미지 5
    SoluImg6 = models.CharField(max_length=255, blank=True, null=True)                              # 솔루션 이미지 6
    userPK = models.CharField(max_length=150, blank=True, null=True)                                # 유저 PK 값

class UserEthWallet(models.Model):
    userPK = models.CharField(max_length=255, blank=True, null=True)
    userAddr = models.CharField(max_length=255, blank=True, null=True)
    fromAddr = models.CharField(max_length=255, blank=True, null=True)
    toAddr = models.CharField(max_length=255, blank=True, null=True)
    eth = models.CharField(max_length=255, null=True, default = "0")
    submitDate = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True, default = "0")
    blockHash = models.CharField(max_length=255, blank=True, null=True)
    blockNumber = models.CharField(max_length=255, blank=True, null=True)
    confirmations = models.CharField(max_length=255, blank=True, null=True)
    contractAddress = models.CharField(max_length=255, blank=True, null=True)
    cumulativeGasUsed = models.CharField(max_length=255, blank=True, null=True)
    gas = models.CharField(max_length=255, blank=True, null=True)
    gasPrice = models.CharField(max_length=255, blank=True, null=True)
    gasUsed = models.CharField(max_length=255, blank=True, null=True)
    hash = models.CharField(max_length=255, blank=True, null=True)
    input = models.CharField(max_length=255, blank=True, null=True)
    isError = models.CharField(max_length=255, blank=True, null=True)
    nonce = models.CharField(max_length=255, blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    transactionIndex = models.CharField(max_length=255, blank=True, null=True)
    txreceipt_status = models.CharField(max_length=255, blank=True, null=True)

class UsergdscWallet(models.Model):
    userPK = models.CharField(max_length=255, blank=True, null=True)
    blockHash = models.CharField(max_length=255, blank=True, null=True)
    blockNumber = models.CharField(max_length=255, blank=True, null=True)
    confirmations = models.CharField(max_length=255, blank=True, null=True)
    cumulativeGasUsed = models.CharField(max_length=255, blank=True, null=True)
    fromAddr = models.CharField(max_length=255, blank=True, null=True)
    gas = models.CharField(max_length=255, blank=True, null=True)
    gasPrice = models.CharField(max_length=255, blank=True, null=True)
    gasUsed = models.CharField(max_length=255, blank=True, null=True)
    hash = models.CharField(max_length=255, blank=True, null=True)
    input = models.CharField(max_length=255, blank=True, null=True)
    nonce = models.CharField(max_length=255, blank=True, null=True)
    timeStamp = models.CharField(max_length=255, blank=True, null=True)
    to = models.CharField(max_length=255, blank=True, null=True)
    tokenDecimal = models.CharField(max_length=255, blank=True, null=True)
    tokenName = models.CharField(max_length=255, blank=True, null=True)
    tokenSymbol = models.CharField(max_length=255, blank=True, null=True)
    transactionIndex = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    datetime = models.CharField(max_length=255, blank=True, null=True)

class ChangeWallet(models.Model):
    userPK = models.CharField(max_length=255, blank=True, null=True)
    gdst = models.CharField(max_length=255, blank=True, null=True)
    gdsc = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True, default = "0")   #(1 = GDST -> GDSC)  (2 = GDSC -> GDST)
    timeStamp = models.CharField(max_length=255, blank=True, null=True)

class UserPoint(models.Model):
    userPK = models.CharField(max_length=255, blank=True, null=True)
    point = models.CharField(max_length=255, blank=True, null=True, default = "0")

class adminDB(models.Model):                                                                        # 어드민 DB
    adminEmail = models.CharField(max_length=250)                                                       # 어드민 ID (이메일 형식)
    password = models.CharField(max_length=250)                                                         # 어드민 비밀번호
    otpCode = models.CharField(max_length=255, blank=True, null=True)                                   # 어드민의 OTP 코드    
