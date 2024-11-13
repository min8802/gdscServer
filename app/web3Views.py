from django.shortcuts import render
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from datetime import datetime, timedelta, date
from django.forms.models import model_to_dict
from bson import json_util
# from web3 import Web3, EthereumTesterProvider
# from web3 import Web3, HTTPProvider, IPCProvider
from web3 import Web3, HTTPProvider, IPCProvider
from eth_account import Account
from eth_keyfile import create_keyfile_json
from hexbytes import HexBytes
from .models import *
from .forms import *
import os
import sys
import json
import hmac, base64, struct, hashlib, time, requests
import getpass

# web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/ace3b880ffb643a9b3db09719d89c3bd'))
# web3 = Web3(IPCProvider("/mnt/hddmnt/geth/sealer1/geth.ipc"))

web3 = Web3(IPCProvider("/mnt/geth.ipc"))
# web3 = Web3(IPCProvider("/mnt/rinke/geth.ipc"))




tokenContract = web3.eth.contract(abi=[{"constant":True,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_who","type":"address"}],"name":"meltAddress","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"who","type":"address"}],"name":"superVoteAgree","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[],"name":"voteAgree","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_hoarder","type":"address"},{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"superApprove","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"open_free","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"to","type":"address"},{"name":"token_amount","type":"uint256"},{"name":"freeze_timestamp","type":"uint256"}],"name":"mintToken","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_index","type":"uint256"},{"name":"bonus_rate","type":"uint8"}],"name":"changeSaleBonusRate","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_proposal_index","type":"uint256"}],"name":"getProposalVoterList","outputs":[{"name":"","type":"address[]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"total_supply","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"getAddressLength","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"to","type":"address"},{"name":"token_amount","type":"uint256"},{"name":"freeze_timestamp","type":"uint256"}],"name":"superMint","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_proposal_index","type":"uint256"}],"name":"getProposalIndex","outputs":[{"name":"generator","type":"address"},{"name":"descript","type":"string"},{"name":"start_timestamp","type":"uint256"},{"name":"end_timestamp","type":"uint256"},{"name":"executed","type":"bool"},{"name":"voting_count","type":"uint256"},{"name":"total_weight","type":"uint256"},{"name":"voting_cut","type":"uint256"},{"name":"threshold","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_index","type":"uint256"},{"name":"sell_token_limit","type":"uint256"}],"name":"changeSaleTokenLimit","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_index","type":"uint256"}],"name":"getSaleSold","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_tos","type":"address[]"},{"name":"_amounts","type":"uint256[]"}],"name":"mintTokenBulk","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_address_index","type":"uint256"}],"name":"getAddressIndex","outputs":[{"name":"_address","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_index","type":"uint256"}],"name":"getSaleInfo","outputs":[{"name":"sale_number","type":"uint256"},{"name":"start_timestamp","type":"uint256"},{"name":"end_timestamp","type":"uint256"},{"name":"bonus_rate","type":"uint8"},{"name":"sell_limit","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"newTokenWallet","type":"address"}],"name":"tokenWalletChange","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"token_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"getAllAddress","outputs":[{"name":"","type":"address[]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_sender","type":"address"}],"name":"checkFreeze","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_index","type":"uint256"},{"name":"end_timestamp","type":"uint256"}],"name":"changeSaleEnd","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[],"name":"tokenOpen","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"getProposalLength","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"who","type":"address"},{"name":"descript","type":"string"},{"name":"start_timestamp","type":"uint256"},{"name":"end_timestamp","type":"uint256"},{"name":"voting_cut","type":"uint256"},{"name":"threshold","type":"uint256"}],"name":"newVote","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_index","type":"uint256"},{"name":"start_timestamp","type":"uint256"},{"name":"end_timestamp","type":"uint256"},{"name":"bonus_rate","type":"uint8"},{"name":"sell_token_limit","type":"uint256"}],"name":"changeSaleInfo","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"tos","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"transferBulk","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"token_wallet_address","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_who","type":"address"},{"name":"_amount","type":"uint256"}],"name":"burn","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_target","type":"address"}],"name":"getAddressExist","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"to","type":"address"},{"name":"value","type":"uint256"}],"name":"transfer","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[],"name":"transferClose","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"canSaleInfo","outputs":[{"name":"sale_number","type":"uint256"},{"name":"start_timestamp","type":"uint256"},{"name":"end_timestamp","type":"uint256"},{"name":"bonus_rate","type":"uint8"},{"name":"sell_limit","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"newName","type":"string"}],"name":"changeTokenName","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[],"name":"checkVote","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[],"name":"tokenClose","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"transfer_close","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"start_timestamp","type":"uint256"},{"name":"end_timestamp","type":"uint256"},{"name":"bonus_rate","type":"uint8"},{"name":"sell_token_limit","type":"uint256"}],"name":"newSale","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_who","type":"address"},{"name":"_addTimestamp","type":"uint256"}],"name":"freezeAddress","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[],"name":"voteClose","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"newSymbol","type":"string"}],"name":"changeTokenSymbol","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[],"name":"transferOpen","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"","type":"address"}],"name":"freezeDateOf","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_conversion_rate","type":"uint256"}],"name":"changeConversionRate","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_index","type":"uint256"},{"name":"start_timestamp","type":"uint256"}],"name":"changeSaleStart","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"conversion_rate","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_hoarder","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"getSaleLength","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_addition","type":"uint256"}],"name":"additionalTotalSupply","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_tos","type":"address[]"},{"name":"_amounts","type":"uint256[]"}],"name":"superMintBulk","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_owner_address","type":"address"},{"name":"_token_wallet_address","type":"address"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"payable":True,"stateMutability":"payable","type":"fallback"},{"anonymous":False,"inputs":[{"indexed":True,"name":"who","type":"address"},{"indexed":False,"name":"eth_amount","type":"uint256"}],"name":"Payable","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"from","type":"address"},{"indexed":True,"name":"to","type":"address"},{"indexed":False,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"from","type":"address"},{"indexed":False,"name":"value","type":"uint256"}],"name":"Burn","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"to","type":"address"},{"indexed":False,"name":"value","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"name":"vote_id","type":"uint256"},{"indexed":False,"name":"generator","type":"address"},{"indexed":False,"name":"descript","type":"string"}],"name":"ProposalAdd","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"name":"vote_id","type":"uint256"},{"indexed":False,"name":"descript","type":"string"}],"name":"ProposalEnd","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"who","type":"address"}],"name":"ChangeTokenName","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"who","type":"address"}],"name":"ChangeTokenSymbol","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"from","type":"address"},{"indexed":True,"name":"to","type":"address"}],"name":"ChangeTokenWalletAddress","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"from","type":"uint256"},{"indexed":True,"name":"to","type":"uint256"}],"name":"ChangeTotalSupply","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"from","type":"uint256"},{"indexed":True,"name":"to","type":"uint256"}],"name":"ChangeConversionRate","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"from","type":"uint256"},{"indexed":True,"name":"to","type":"uint256"}],"name":"ChangeFreezeTime","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"_who","type":"address"},{"indexed":False,"name":"_date","type":"uint256"}],"name":"Freeze","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"_who","type":"address"}],"name":"Melt","type":"event"}])
# # abi = json.loads('<Enter copied ABI here>')
# # address=web3.toChecksumAddress("0xcb838939836300c3cb1cf613f9607ea42cf521b9")
# # contract=w3.eth.contract(address=address, abi=abi)
# address=web3.toChecksumAddress("0xcb838939836300c3cb1cf613f9607ea42cf521b9")
# TokenC_I = tokenContract(address=address)

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


@csrf_exempt
def newAccount(request):
    try:
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("web3 - Connection : ", web3.isConnected())
        # userID = request.POST.get('userID')
        # addr = web3.geth.personal.newAccount('asd123!')

        # userinfo = SignUp.objects.get(id = userID)
        # userCheck = userinfo.oneMoreCheck
        # if userCheck == "0":
        #     # 일반유저
        #     userinfo.ethAddr = addr
        #     # userinfo.vicAddr = addr
        #     userinfo.userWalletMakeTime = datetime.now()
        #     userinfo.save()
        #     print(userinfo.username + " 님 유저 계좌 생성 완료 : " + addr)
        # elif userCheck == "1":
        #     # 작가
        #     artiinfo = AuthorList.objects.get(userPK = userID)
        #     artiinfo.ethAddr = addr
        #     artiinfo.authorWalletMakeTime = datetime.now()
        #     artiinfo.save()
        #     print(userinfo.username + " 님 작가 계좌 생성 완료 : " + addr)
        # print("-----------------------------------------------------------------------------------------------------------------------------")
        context = {'value':'1'}
        return HttpResponse(json.dumps(context))
    except Exception as error:
        print(error)
        context = {'value':'-99'}
        return HttpResponse(json.dumps(context))



@csrf_exempt
def userSendVic(request):
    try:
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("web3 - Connection : ", web3.isConnected())
        userID = request.POST.get('userID')
        toAddr = request.POST.get('toAddr')
        addrEth = request.POST.get('addrEth')
        # toAddr = "0xE187248a9B33d1Ea0557efBA5FD02d398e532799"
        # ----------------------------------------------------------------------------------------
        # fromAddr = "0xf1AbE0E699B5404785a140863428e1Cb5715B2d5" # 아르떼 모 지갑 주소
        fromAddr = "0xd3e2372b19D463D507272A6B1D9c72C792E8FBAD" # 테스트넷 eth 있는 계좌
        # ----------------------------------------------------------------------------------------
        # fromAddr = "0x2f2427CE4b91614903BA4Bf4ff3d624FE6F48362"


        fromAddrChecksum = web3.toChecksumAddress(fromAddr)
        toAddrChecksum = web3.toChecksumAddress(toAddr)

		# 토큰 출금
        TokenC_I = tokenContract(address=web3.toChecksumAddress("0xb708925e5136e88b3b5fc078404795d025e04134"))
        print("TokenC_I ::", TokenC_I)
        print(tokenContract)
        unRock = web3.geth.personal.unlockAccount(fromAddrChecksum, "asd123!", 10)
        print(unRock)
        print(web3.toWei(1,"ether"))
        # print("1111111",TokenC_I.transact({'gas' : 4700000, "from": fromAddrChecksum}))
        test = TokenC_I.functions.transfer(toAddrChecksum, web3.toWei(1,"ether")).transact({'gas' : 400000, "from": fromAddrChecksum})
        print(test.hex())
        rock = web3.geth.personal.lockAccount(fromAddrChecksum)
        # print(rock)
		# ---------------------------------------------------------------------------------------------------------------------------------------
        print("-----------------------------------------------------------------------------------------------------------------------------")
        context = {'value':'1'}
        return HttpResponse(json.dumps(context))
    except Exception as error:
        print(error)
        context = {'value':'-99'}
        return HttpResponse(json.dumps(context))


# @csrf_exempt
# def authorSendVic(request):
#     try:
#         print("-----------------------------------------------------------------------------------------------------------------------------")
#         print("web3 - Connection : ", web3.isConnected())
#         userID = request.POST.get('userID')
#         toAddr = request.POST.get('toAddr')
#         # toAddr = "0xE187248a9B33d1Ea0557efBA5FD02d398e532799"
#
#
#         # ----------------------------------------------------------------------------------------
#         # fromAddr = "0xf1AbE0E699B5404785a140863428e1Cb5715B2d5" # 아르떼 모 지갑 주소
#         fromAddr = "0xd3e2372b19D463D507272A6B1D9c72C792E8FBAD" # 테스트넷 eth 있는 계좌
#         # ----------------------------------------------------------------------------------------
#
#
#         # fromAddr = "0x2f2427CE4b91614903BA4Bf4ff3d624FE6F48362"
#         # toAddr = request.POST.get('toAddr')
#         # toAddr = "0xE187248a9B33d1Ea0557efBA5FD02d398e532799"
#         #
#         # fromAddr = "0x2f2427CE4b91614903BA4Bf4ff3d624FE6F48362"
#
#
#
#         fromAddrChecksum = web3.toChecksumAddress(fromAddr)
#         toAddrChecksum = web3.toChecksumAddress(toAddr)
#
# 		# 토큰 출금
#         TokenC_I = tokenContract(address=web3.toChecksumAddress("0xb708925e5136e88b3b5fc078404795d025e04134"))
#         print("TokenC_I ::", TokenC_I)
#         print(tokenContract)
#         unRock = web3.geth.personal.unlockAccount(fromAddrChecksum, "asd123!", 10)
#         print(unRock)
#         print(web3.toWei(1,"ether"))
#         # print("1111111",TokenC_I.transact({'gas' : 4700000, "from": fromAddrChecksum}))
#         test = TokenC_I.functions.transfer(toAddrChecksum, web3.toWei(1,"ether")).transact({'gas' : 400000, "from": fromAddrChecksum})
#         print(test.hex())
#         rock = web3.geth.personal.lockAccount(fromAddrChecksum)
#         # print(rock)
# 		# ---------------------------------------------------------------------------------------------------------------------------------------
#         print("-----------------------------------------------------------------------------------------------------------------------------")
#         context = {'value':'1'}
#         return HttpResponse(json.dumps(context))
#     except Exception as error:
#         print(error)
#         context = {'value':'-99'}
#         return HttpResponse(json.dumps(context))



@csrf_exempt
def authorSendVic(request):
    try:
        userID = request.POST.get('userID')
        toAddr = request.POST.get('toAddr')
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("web3 - Connection : ", web3.isConnected())


        # ----------------------------------------------------------------------------------------
        # fromAddr = "0xf1AbE0E699B5404785a140863428e1Cb5715B2d5" # 아르떼 모 지갑 주소
        fromAddr = "0xd3e2372b19D463D507272A6B1D9c72C792E8FBAD" # 테스트넷 eth 있는 계좌
        # ----------------------------------------------------------------------------------------

        fromAddrChecksum = web3.toChecksumAddress(fromAddr)
        toAddrChecksum = web3.toChecksumAddress(toAddr)

		# 토큰 출금
        TokenC_I = tokenContract(address=web3.toChecksumAddress("0xb708925e5136e88b3b5fc078404795d025e04134"))
        print("TokenC_I ::", TokenC_I)
        print(tokenContract)
        unRock = web3.geth.personal.unlockAccount(fromAddrChecksum, "asd123!", 10)
        print(unRock)
        print(web3.toWei(1,"ether"))
        test = TokenC_I.functions.transfer(toAddrChecksum, web3.toWei(1,"ether")).transact({'gas' : 400000, "from": fromAddrChecksum})
        print(test.hex())
        rock = web3.geth.personal.lockAccount(fromAddrChecksum)

        print("-----------------------------------------------------------------------------------------------------------------------------")


        context = {'value':'1'}
        return HttpResponse(json.dumps(context))
    except Exception as error:
        print(error)
        context = {'value':'-99'}
        return HttpResponse(json.dumps(context))



@csrf_exempt
def userSendEth(request):
    try:
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("web3 - Connection : ", web3.isConnected())
        userID = request.POST.get('userID')
        toAddr = request.POST.get('toAddr')
        addrEth = request.POST.get('addrEth')
        # toAddr = "0xE187248a9B33d1Ea0557efBA5FD02d398e532799"

        # fromAddr = "0x2f2427CE4b91614903BA4Bf4ff3d624FE6F48362"

        # # ----------------------------------------------------------------------------------------
        # # fromAddr = "0xf1AbE0E699B5404785a140863428e1Cb5715B2d5" # 아르떼 모 지갑 주소
        # fromAddr = "0xd3e2372b19D463D507272A6B1D9c72C792E8FBAD" # 테스트넷 eth 있는 계좌
        # # ----------------------------------------------------------------------------------------
        #
        #
        # fromAddrChecksum = web3.toChecksumAddress(fromAddr)
        # toAddrChecksum = web3.toChecksumAddress(toAddr)
        #
        # # 중요함
        # sendTx = web3.geth.personal.sendTransaction({
        #     "from": fromAddrChecksum,
        #     "gasPrice": "20000000000",
        #     "gas": "21000",
        #     "to": toAddrChecksum,
        #     "value": "10000000000000000000",
        #     "data": ""
        # }, 'asd123!').then(console.log);
        # print(sendTx)

        toAddr = "0x38738AA79002bFb3F96dfd843D1Eb58E3B80AB68"   # 실제로는 이부분 주석
        fromAddr = "0xd3e2372b19D463D507272A6B1D9c72C792E8FBAD"
        fromCheckSumAddr = web3.toChecksumAddress(fromAddr)
        toCheckSumAddr = web3.toChecksumAddress(toAddr)
        # eth.gasprice
        # 중요함
        getPrice = web3.eth.gasPrice;
        print(getPrice)
        addrEth = addrEth * 1000000000000000000
        sendTx = web3.geth.personal.sendTransaction({
            "from": fromCheckSumAddr,
            "gasPrice": getPrice,
            "gas": "80000",
            "to": toCheckSumAddr,
            "value": addrEth,
            "data": ""
        }, 'asd123!')




# 가나치

		# # 토큰 출금
        # TokenC_I = tokenContract(address=web3.toChecksumAddress("0xb708925e5136e88b3b5fc078404795d025e04134"))
        # print("TokenC_I ::", TokenC_I)
        # print(tokenContract)
        # unRock = web3.geth.personal.unlockAccount(fromAddrChecksum, "asd123!", 10)
        # print(unRock)
        # print(web3.toWei(1,"ether"))
        # # print("1111111",TokenC_I.transact({'gas' : 4700000, "from": fromAddrChecksum}))
        # test = TokenC_I.functions.transfer(toAddrChecksum, web3.toWei(1,"ether")).transact({'gas' : 400000, "from": fromAddrChecksum})
        # print(test.hex())
        # rock = web3.geth.personal.lockAccount(fromAddrChecksum)
        # # print(rock)
		# # ---------------------------------------------------------------------------------------------------------------------------------------
        print("-----------------------------------------------------------------------------------------------------------------------------")
        context = {'value':'1'}
        return HttpResponse(json.dumps(context))
    except Exception as error:
        print(error)
        context = {'value':'-99'}
        return HttpResponse(json.dumps(context))


@csrf_exempt
def authorSendEth(request):
    try:
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("web3 - Connection : ", web3.isConnected())
        userID = request.POST.get('userID')
        toAddr = request.POST.get('toAddr')
        addrEth = request.POST.get('addrEth')
        # toAddr = "0xE187248a9B33d1Ea0557efBA5FD02d398e532799"

        # fromAddr = "0x2f2427CE4b91614903BA4Bf4ff3d624FE6F48362"

        # ----------------------------------------------------------------------------------------
        # # fromAddr = "0xf1AbE0E699B5404785a140863428e1Cb5715B2d5" # 아르떼 모 지갑 주소
        # fromAddr = "0xd3e2372b19D463D507272A6B1D9c72C792E8FBAD" # 테스트넷 eth 있는 계좌
        # ----------------------------------------------------------------------------------------

        toAddr = "0x38738AA79002bFb3F96dfd843D1Eb58E3B80AB68"   # 실제로는 이부분 주석
        fromAddr = "0xd3e2372b19D463D507272A6B1D9c72C792E8FBAD"

        fromAddrChecksum = web3.toChecksumAddress(fromAddr)
        toAddrChecksum = web3.toChecksumAddress(toAddr)

        # 중요함
        getPrice = web3.eth.gasPrice;
        print(getPrice)
        addrEth = addrEth * 1000000000000000000
        sendTx = web3.geth.personal.sendTransaction({
            "from": fromAddrChecksum,
            "gasPrice": getPrice,
            "gas": "80000",
            "to": toAddrChecksum,
            "value": addrEth,
            "data": ""
        }, 'asd123!').then(console.log);
        print(sendTx)

# 가나치

		# # 토큰 출금
        # TokenC_I = tokenContract(address=web3.toChecksumAddress("0xb708925e5136e88b3b5fc078404795d025e04134"))
        # print("TokenC_I ::", TokenC_I)
        # print(tokenContract)
        # unRock = web3.geth.personal.unlockAccount(fromAddrChecksum, "asd123!", 10)
        # print(unRock)
        # print(web3.toWei(1,"ether"))
        # # print("1111111",TokenC_I.transact({'gas' : 4700000, "from": fromAddrChecksum}))
        # test = TokenC_I.functions.transfer(toAddrChecksum, web3.toWei(1,"ether")).transact({'gas' : 400000, "from": fromAddrChecksum})
        # print(test.hex())
        # rock = web3.geth.personal.lockAccount(fromAddrChecksum)
        # # print(rock)
		# # ---------------------------------------------------------------------------------------------------------------------------------------
        print("-----------------------------------------------------------------------------------------------------------------------------")
        context = {'value':'1'}
        return HttpResponse(json.dumps(context))
    except Exception as error:
        print(error)
        context = {'value':'-99'}
        return HttpResponse(json.dumps(context))
# @csrf_exempt
# def web3Test(request):
#     try:
#         print("-----------------------------------------------------------------------------------------------------------------------------")
#
#         print("tokenContract ::", tokenContract)
#         print("web3 - Connection : ", web3.isConnected())
#         print("web3", web3)
#
#         print("web3.eth.contract ::", web3.eth.contract())
#
#         fromEthAddr = "0x20f77b9c8bdff86352191d99614d7d67be22f1ba"
#         fromCheckSumAddr = web3.toChecksumAddress(fromEthAddr)
#         toEthAddr = "0x5c079c4b0762c31c4e6a086fda91da692a8c572c"
#         toCheckSumAddr = web3.toChecksumAddress(toEthAddr)
#
#         fromBalance = web3.eth.getBalance(fromCheckSumAddr)
#         toBalance = web3.eth.getBalance(toCheckSumAddr)
#         print("fromBalance==", fromBalance)
#         print("toBalance==", toBalance)
#
#
#         Tx = (TokenC_I.transact({'gas' : 4700000, "from": fromCheckSumAddr}).transferFrom(toCheckSumAddr,fromCheckSumAddr,value)).hex()
#         print(Tx)
#         print("-----------------------------------------------------------------------------------------------------------------------------")
#
#         context = {'value':'1'}
#         return HttpResponse(json.dumps(context))
#     except Exception as error:
#         print(error)
#         context = {'value':'-99'}
#         return HttpResponse(json.dumps(context))


# @csrf_exempt
# def newAccount(request):
#     try:
#         # web3 = Web3(HTTPProvider('http://49.247.195.91:8545'))
#         # web3 = Web3(HTTPProvider('http://192.168.0.145:8545'))
#         print("-----------------------------------------------------------------------------------------------------------------------------")
#         # print("TokenC_I::", TokenC_I)
#         # print("tokenContract ::", tokenContract)
#         print("web3 - Connection : ", web3.isConnected())
#         # print("web3", web3)
#         # aa = Account.create('asd123!')
#         # print(aa.address)
#
#         # web3.eth.accounts.create();
#         # {
#         #     address: "0xe78150FaCD36E8EB00291e251424a0515AA1FF05",
#         #     privateKey: "0xcc505ee6067fba3f6fc2050643379e190e087aeffe5d958ab9f2f3ed3800fa4e",
#         #     signTransaction: function(tx){...},
#         #     sign: function(data){...},
#         #     encrypt: function(password){...}
#         # }
#         # --------------------------------------------------------------------------------------
#         # bb = web3.eth.account.create()
#         # addr = bb.address
#         # privateKey = bb.privateKey.hex()
#         # print(bb.address)
#         # print(bb.privateKey.hex())
#         # dd = web3.eth.account.privateKeyToAccount(privateKey)
#         # print(dd)
#         # --------------------------------------------------------------------------------------
#         # encrypted={
#         #     'address': bb.address,
#         #     'crypto': {
#         #         'cipher': 'aes-128-ctr',
#         #         'cipherparams': {
#         #             'iv': '78f214584844e0b241b433d7c3bb8d5f'
#         #         },
#         #         'ciphertext': 'd6dbb56e4f54ba6db2e8dc14df17cb7352fdce03681dd3f90ce4b6c1d5af2c4f',
#         #         'kdf': 'pbkdf2',
#         #         'kdfparams': {
#         #             'c': 1000000,
#         #             'dklen': 32,
#         #             'prf': 'hmac-sha256',
#         #             'salt': '45cf943b4de2c05c2c440ef96af914a2'
#         #         },
#         #         'mac': 'f5e1af09df5ded25c96fcf075ada313fb6f79735a914adc8cb02e8ddee7813c3'
#         #         },
#         #         'id': 'b812f3f9-78cc-462a-9e89-74418aa27cb0',
#         #         'version': 3
#         # }
#         # dd = web3.eth.account.decrypt(encrypted, getpass.getpass())
#         # print(dd)
#
#
#
#         # url = 'http://192.168.0.145:8545'
#         # headers = {"Content-Type": "application/json",}
#         # data = {"jsonrpc":"2.0","method":"web3_clientVersion","params": [],"id":67}
#         # aa = requests.post(url, data=json.dumps(data), headers=headers)
#         # aa = json.dumps(aa)
#
#         # json_data = {
#         #     'jsonrpc': '2.0',
#         #     'method': 'web3_clientVersion',
#         #     'params': [],
#         #     'id': 67,
#         # }
#         #
#         # response = requests.post('http://192.168.0.146:8545/', json=json_data)
#         # print(response)
#         # _keystore_file()
#         # print("web3.eth.contract ::", web3.eth.contract())
#
#
#
#         # with open('~/.ethereum/keystore/UTC--...4909639D2D17A3F753ce7d93fa0b9aB12E') as keyfile:
#         #     encrypted_key = keyfile.read()
#         #     private_key = web3.eth.account.decrypt(encrypted_key, 'correcthorsebatterystaple')
# # address2 = Web3.toChecksumAddress('0x2551d2357c8da54b7d330917e0e769d33f1f5b93')
# # balance=contract.functions.balanceOf(address2).call()
#         # fromEthAddr = "0x20f77b9c8bdff86352191d99614d7d67be22f1ba"
#         # fromCheckSumAddr = web3.toChecksumAddress(fromEthAddr)
#         # toEthAddr = "0x5c079c4b0762c31c4e6a086fda91da692a8c572c"
#         # toCheckSumAddr = web3.toChecksumAddress(toEthAddr)
#         # # tt = web3.eth.sendTransaction({
#         # #     "from": fromCheckSumAddr,
#         # #     "to": toCheckSumAddr,
#         # #     "value": '1000000000000000'
#         # # })
#         # # print(tt)
#         # value = web3.fromWei(0.001,"ether")
#         #
#
#         # fromBalance = web3.eth.getBalance(fromCheckSumAddr)
#         # toBalance = web3.eth.getBalance(toCheckSumAddr)
#         # print("fromBalance==", fromBalance)
#         # print("toBalance==", toBalance)
#
#         # print("TokenC_I", TokenC_I.token_amount(fromCheckSumAddr))
#         # sendTransbal = web3.fromWei(fromBalance,"ether")
#         # print("sendTransbal :;", sendTransbal)
#         # test = web3.fromWei(1000000000000000,"ether")
#         # print(test)
#         # # print(web3.eth_coinbase())
#         # aa = web3.eth.personal.sign("Hello", toEthAddr, "311179482")
#         # print(aa)
#         # signed_txn = web3.eth_signTransaction(dict(
#         #     nonce=web3.eth.get_transaction_count(toCheckSumAddr),
#         #     maxFeePerGas=2000000000,
#         #     maxPriorityFeePerGas=1000000000,
#         #     gas=100000,
#         #     to=toCheckSumAddr,
#         #     value=1,
#         #     data=b'',
#         #     )
#         # )
#         # print(signed_txn)
#         # web3.eth.send_transaction({
#         #   'to': fromCheckSumAddr,
#         #   'from': toCheckSumAddr,
#         #   'value': 1000000000000000,
#         #   'gas': 21000,
#         #   'gasPrice': web3.toWei(50, 'gwei'),
#         # })
#
#         # nonce = web3.eth.getTransactionCount(fromCheckSumAddr);
#         # gasPrice = web3.eth.gasPrice;
#         # value = web3.toWei(0.00001, 'ether');
#         # gasLimit = web3.eth.estimateGas({ "to": toCheckSumAddr, "from": fromCheckSumAddr, "value": value }); # the used gas for the simulated call/transaction (,,21000)
#         # txObject = {
#         #     "nonce": nonce,
#         #     "gasPrice": gasPrice,
#         #     "gasLimit": gasLimit,
#         #     "to": toCheckSumAddr,
#         #     "from": fromCheckSumAddr,
#         #     "value": value
#         # };
#         # transactionHash = web3.eth.sendTransaction(txObject);
#
#
#         # Tx = (TokenC_I.transact({'gas' : 4700000, "from": fromCheckSumAddr}).transferFrom(toCheckSumAddr,fromCheckSumAddr,value)).hex()
#         # print(Tx)
#         print("-----------------------------------------------------------------------------------------------------------------------------")
#
#         context = {'value':'1'}
#         return HttpResponse(json.dumps(context))
#     except Exception as error:
#         print(error)
#         context = {'value':'-99'}
#         return HttpResponse(json.dumps(context))
# def _keystore_file(self):
#     keystore_path = self._datadir.join('keys')
#     print("keystore_path ::", keystore_path)
#     keystore_path.mkdir(exist_ok=True, parents=True)
#     keystore_file = keystore_path.joinpath('UTC--1')
#     if not keystore_file.exists():
#         log.debug('Initializing keystore', node=self._index)
#         gevent.sleep()
#         privkey = hashlib.sha256(
#         f'{self._runner.scenario_name}-{self._index}'.encode(),
#         ).digest()
#         keystore_file.write_text(json.dumps(create_keyfile_json(privkey, b'')))
#     return keystore_file
# def encrypt(private_key, password):
#     key_bytes = HexBytes(private_key)
#     password_bytes = text_if_str(to_bytes, password)
#     assert len(key_bytes) == 32
#     return create_keyfile_json(key_bytes, password_bytes)


@csrf_exempt
def testnet(request):
    try:
        # print("-----------------------------------------------------------------------------------------------------------------------------")
        # 정상코드 - 2022.04.04 - JJS
        # print("web3 - Connection : ", web3.isConnected())
        # addr = web3.geth.personal.newAccount('asd123!')
        # print(addr)
        # # aa = web3.toChecksumAddress("0xB9d09c285F8cE6A7C6668ab107756A4b10ABc4A1")
        # # bb = web3.eth.getBalance(aa)
        # # cc = bb / 1000000000000000000
        # # print(cc)
        #
        # toAddr = "0x38738AA79002bFb3F96dfd843D1Eb58E3B80AB68"
        # fromAddr = "0xd3e2372b19D463D507272A6B1D9c72C792E8FBAD"
        # fromCheckSumAddr = web3.toChecksumAddress(fromAddr)
        # toCheckSumAddr = web3.toChecksumAddress(toAddr)
        # # eth.gasprice
        # # 중요함
        # getPrice = web3.eth.gasPrice;
        # print(getPrice)
        # sendTx = web3.geth.personal.sendTransaction({
        #     "from": fromCheckSumAddr,
        #     "gasPrice": getPrice,
        #     "gas": "80000",
        #     "to": toCheckSumAddr,
        #     "value": "100000000000000",
        #     "data": ""
        # }, 'asd123!')
        #
        # print("-----------------------------------------------------------------------------------------------------------------------------")

        # print("-----------------------------------------------------------------------------------------------------------------------------")
        # # arte 모계좌 unLock 테스트 정상 작동 - 2022.04.04 - JJS
        # fromAddr = "0xf1AbE0E699B5404785a140863428e1Cb5715B2d5"
        # fromCheckSumAddr = web3.toChecksumAddress(fromAddr)
        # unLock = web3.geth.personal.unlockAccount(fromCheckSumAddr, "ARTEvic6599!", 10)
        # print(unLock)
        # lock = web3.geth.personal.lockAccount(fromCheckSumAddr)
        # print(lock)
        # print("-----------------------------------------------------------------------------------------------------------------------------")

        context = {'value':'1'}
        return HttpResponse(json.dumps(context))
    except Exception as error:
        print(error)
        context = {'value':'-99'}
        return HttpResponse(json.dumps(context))
