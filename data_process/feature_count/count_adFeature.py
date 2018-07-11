words=[]
with open ("/home/jx/Documents/adFeature.csv") as f:
    i = 0
    for line in f.readlines():
        if "id" not in line:
            words.append(line.strip("\n").split(","))
            i+=1
    aid=[]
    advertiserId=[]
    campaignId=[]
    creativeId=[]
    creativeSize=[]
    adCategoryId=[]
    productId=[]
    productType=[]
    for j in range(i):
        if words[j][0] not in aid:
            aid.append(words[j][0])
        if words[j][1] not in advertiserId:
            advertiserId.append(words[j][1])
        if words[j][2] not in campaignId:
            campaignId.append(words[j][2])
        if words[j][3] not in creativeId:
            creativeId.append(words[j][3])
        if words[j][4] not in creativeSize:
            creativeSize.append(words[j][4])
        if words[j][5] not in adCategoryId:
            adCategoryId.append(words[j][5])
        if words[j][6] not in productId:
            productId.append(words[j][6])
        if words[j][7] not in productType:
            productType.append(words[j][7])
    print len(aid)
    print len(advertiserId)
    print len(campaignId)
    print len(creativeId)
    print len(creativeSize)
    print len(adCategoryId)
    print len(productId)
    print len(productType)