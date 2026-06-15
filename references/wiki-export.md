# 2026 年美国 Foreign\-owned U\.S\. DE LLC 的 IRS 信息申报DIY

Imported from: https://t02xmt66jgr.feishu.cn/wiki/Ei91wxkxSistBkkBHDrc29bMnah
Imported at UTC: 2026-06-15T04:15:30.987309+00:00

---

# 2026 年美国 Foreign\-owned U\.S\. DE LLC 的 IRS 信息申报DIY 

https://irs\.gov/form5472

https://irs\.gov/form1120

# 为什么要交 Form 5472  \+ Pro Forma Form 1120

因为对 **foreign\-owned U\.S\. DE** 来说，IRS 要解决的是 **信息披露**，不是把这个实体当成一个真正单独纳税的 corporation 去算企业所得税。

核心逻辑就两步。



第一步，**为什么需要交 Form 5472**。
IRS 依据 **section 6038A** 的规则，把“由外国人全资持有的美国 disregarded entity”在**有限目的**下视为一个独立于 owner 的 domestic corporation，用来披露它与外国 owner / 关联方之间的 **reportable transactions**。IRS 在 2025 Form 1120 instructions 里写得很清楚：如果外国人全资拥有一个 domestic DE，这个 DE 会为了 6038A 的要求，被当作独立于 owner 的 domestic corporation；虽然 DE 本身一般**不需要报美国所得税申报表**，但如果落入这套规则，就必须提交 **Form 5472**。



第二步，**为什么还要附一份 pro forma Form 1120**。
5472 不是单独裸交的常规表，它通常是“附在 reporting corporation 的 income tax return 后面”。但 foreign\-owned U\.S\. DE 本身又**没有正常的 corporation 所得税申报义务**。所以 IRS 专门设计了一个折中办法：
你不用报一份完整的企业所得税 Form 1120，但**必须交一份 pro forma Form 1120，专门作为 5472 的挂载封面**。IRS 的 5472 instructions 明确说：foreign\-owned U\.S\. DE **has no income tax return filing requirement**，但仍然 **required to file a pro forma Form 1120, with Form 5472 attached**。

这也解释了为什么是 **“需要且只需要 5472 \+ pro forma 1120”**：

- **需要 5472**，因为这是你要履行的核心信息申报义务，目的是披露与外国 owner/关联方的交易。

- **需要 pro forma 1120**，因为 IRS 规定 foreign\-owned U\.S\. DE 的 5472 要附着在这张表上提交。

- **只需要 pro forma 1120，而不是完整 1120**，因为这个 DE 本身并没有企业所得税申报义务。IRS 还进一步限定：对这类 DE，1120 上**只需要填写名称、地址，以及首页指定项目**，不是让你完整填写收入、扣除、税额那一整套 corporation return。

换句话说，**Form 5472 是实体内容，pro forma 1120 是提交载体**。
IRS 不是在要求你把单成员 DE LLC 当成真正的 C corporation 去报税，而是在要求你用 **最小化的 1120 壳子** 把 5472 交上去。

再说得更直白一点：

- 你**不是**因为 LLC 要交企业所得税，所以交 1120；

- 你是因为 **5472 必须挂在 1120 上**，所以才交一个 **pro forma 1120**；

- 这个 1120 本身**不是完整所得税申报表**，只是 IRS 要的“封皮”。

# 概述

1. **Form 1120:** 仅作为封面，写上 "Foreign\-owned U\.S\. DE"，只填基本信息并签字，其余全空。

2. **Form 5472:**

    - **Part I, II, III:** 填好 LLC 和你的基本信息。

    - **Part V:** 统计好这一年：

        - \(A\) 你从个人账户转入 LLC 多少钱（包括 Stripe 账户建立初期的验证费等）。

        - \(B\) LLC 转回给你个人多少钱（或者 Stripe 直接打款到你个人账户的总额）。

    - **申报方式:** 制作一份简单的 **Attachment** 列明 \(A\) 和 \(B\) 的金额。

3. **截止日期:** 次年 4 月 15 日前，**邮寄或传真**给 IRS（同 Form 1120 一起）。



需要信息：

- 公司名

- EIN

- 公司地址（和申请 EIN 时一致）

- 公司成立时间

- 是否是第一次申报或者注销的最后一次申报

- 公司名和公司地址是否有变更

- 个人向公司转账的明细

- 公司向个人转账的明细

- 个人的身份证号

- 个人住址



模版：

\[IRS\_5472\_ProForma1120\_\[ABC\_LLC\]\_TaxYear2025\_Faxed\_2026\-03\-11\(1\)\.pdf\]

将填好的文件[传真](https://app.hellofax.com?ref=5e4eadd6&s=F&utm_medium=social&utm_source=facebooktwitter&utm_campaign=hellofax-incentivized-post&utm_content=hf)（这个链接可以免费发传真）给 IRS，并保存传真成功的回执。

**对 Form 5472 \+ Pro\-Forma 1120 来说：**

👉 **“你成功发送 \+ 留好证据” = IRS 已经收到（法律意义上）**

**美国税法采用的是：Mailbox / Fax Rule**

意思是：

**只要你能证明“在截止日前发送”**
 👉 **即使 IRS 丢件，你也不罚**

所以：

- 你保存的 **fax confirmation**

- 在法律上 **比 IRS 系统记录还重要**

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OTYwZDE5OWViNDUyNDFiMjQ5YTYxMmJiMjRkYzFmZWFfNzFmNmEzODYwZTc0Y2Q1NGExNmIxYjc2ZWJkMTlmZGNfSUQ6NzYxNjI2NzgzODI2NTkzNjg0MF8xNzgxNDk2NjEzOjE3ODE1ODMwMTNfVjM)





下面是一份 **“外国个人 100% 持有的 Delaware 单成员 LLC，全年只有  owner 注资，无分配”** 的 **Form 5472 \+ pro forma Form 1120 逐项样例**。
Form 5472 的相关栏位、Line 2/3、Part II、Part V，以及 pro forma 1120 首页的可填写项，均以 IRS 官方表格和说明为准。\([美国国税局](https://www.irs.gov/pub/irs-pdf/f5472.pdf)\)

---

# 样例设定

- LLC 名称：**MTPARK LLC**

- EIN：**12\-3456789**

- 注册地址：**8 The Green, Suite A, Dover, DE 19901**

- 成立日期：**2025\-03\-01**

- 外国 owner：**San Zhang**

- Owner 地址：**No\. 88 Renmin Road, Dali, Yunnan, China**

- 国籍 / 税务居民国：**China**

- 2025 年唯一关联交易：**2025\-03\-05 owner 注资 USD 10,000**

- 年末总资产：**USD 10,000**

- 主营业务：**Software Publishing**

- 主营业务代码：**513210**。\([美国国税局](https://www.irs.gov/pub/irs-pdf/i1120.pdf)\)

---

# 一、Form 5472 样例

## Part I — Reporting Corporation

**1a Name of reporting corporation**
MTPARK LLC

**Address**
8 The Green, Suite A
Dover, DE 19901
USA

**1b Employer identification number**
12\-3456789

**1c Total assets**
10,000

**1d Principal business activity**
Software Publishing

**1e Principal business activity code**
513210

**1f Total value of gross payments made or received reported on this Form 5472**
10,000

**1g Total number of Forms 5472 filed for the tax year**
1

**1h Total value of gross payments made or received reported on all Forms 5472**
10,000

**1i consolidated filing**
不勾

**1j initial year**
勾选

**1k Total number of Parts VIII attached to Form 5472**
0

**1l Country of incorporation**
United States

**1m Date of incorporation**
03/01/2025

**1n Country\(ies\) under whose laws the reporting corporation files an income tax return as a resident**
留空

**1o Principal country\(ies\) where business is conducted**
United States

**Line 2**
勾选

**Line 3**
勾选。\([美国国税局](https://www.irs.gov/pub/irs-pdf/f5472.pdf)\)

---

## Part II — 25% Foreign Shareholder

### 4a Name and address of direct 25% foreign shareholder

San Zhang

No\. 88 Renmin Road

Dali, Yunnan

China

### 4b\(1\) U\.S\. identifying number, if any

留空

### 4b\(2\) Reference ID number

留空

### 4b\(3\) Foreign taxpayer identification number \(FTIN\), if any

留空

### 4c Principal country\(ies\) where business is conducted

China

### 4d Country of citizenship, organization, or incorporation

China

### 4e Country\(ies\) under whose laws the direct 25% foreign shareholder files an income tax return as a resident

China

**5a–7e**
全部留空。\([美国国税局](https://www.irs.gov/pub/irs-pdf/f5472.pdf)\)

---

## Part III — Related Party

**顶部选择框**
勾选 **foreign person**

### 8a Name and address of related party

San Zhang

No\. 88 Renmin Road

Dali, Yunnan

China

### 8b\(1\) U\.S\. identifying number, if any

留空

### 8b\(2\) Reference ID number

留空

### 8b\(3\) FTIN, if any

留空

### 8c Principal business activity

Individual Investor

### 8d Principal business activity code

留空

### 8e Relationship — Check boxes that apply

- 勾选 **Related to reporting corporation**

- 勾选 **25% foreign shareholder**

- 不勾 **Related to 25% foreign shareholder**

### 8f Principal country\(ies\) where business is conducted

China

### 8g Country\(ies\) under whose laws the related party files an income tax return as a resident

China。\(美国国税局\)

---

## Part IV — Monetary Transactions Between Reporting Corporation and Foreign Related Party

**9–36**
全部填 **0** 或留空。
本样例不在 Part IV 报，唯一关联交易放 Part V。\([美国国税局](https://www.irs.gov/pub/irs-pdf/f5472.pdf)\)

---

## Part V — Reportable Transactions of a Reporting Corporation That Is a Foreign\-Owned U\.S\. DE

**勾选 Part V**

**单独附页内容如下：**

**Part V Attachment**
Reporting Corporation: MTPARK LLC
EIN: 12\-3456789
Tax Year: 01/01/2025 – 12/31/2025

1. On March 5, 2025, the sole foreign owner, San Zhang, made a capital contribution of USD 10,000 to MTPARK LLC in connection with the funding of the entity\.

\(美国国税局\)

---

## Part VI — Nonmonetary and Less\-Than\-Full Consideration Transactions

不勾。\(美国国税局\)

---

## Part VII — Additional Information

**37** No
**38a** No
**38b** 留空
**38c** 留空
**39** No
**40a** No
**40b** 留空
**41a** No
**41b–41d** 留空
**42** No
**43** No。\([美国国税局](https://www.irs.gov/pub/irs-pdf/f5472.pdf)\)

---

# 二、pro forma Form 1120 样例

**表头上方手写 / 打字：**
**Foreign\-owned U\.S\. DE**。\([美国国税局](https://www.irs.gov/pub/irs-pdf/i5472.pdf)\)

**Name**
MTPARK LLC

**Address**
8 The Green, Suite A
Dover, DE 19901
USA

**A**
留空

**B Employer identification number**
12\-3456789

**C Date incorporated**
03/01/2025

**D Total assets**
10,000

**E Check if**
勾选 **\(1\) Initial return**

**1a–31 其余收入、扣除、税额栏**
留空。\([美国国税局](https://www.irs.gov/pub/irs-pdf/i5472.pdf)\)

---

# 三、传真顺序样例

1. Fax Cover Sheet

2. pro forma Form 1120

3. Form 5472

4. Part V Attachment。\([美国国税局](https://www.irs.gov/pub/irs-pdf/i5472.pdf)\)

---

# 四、可直接替换的纯文本模板

```Plain Text
FORM 5472

Part I
1a  MTPARK LLC
    8 The Green, Suite A, Dover, DE 19901, USA
1b  12-3456789
1c  10000
1d  Software Publishing
1e  513210
1f  10000
1g  1
1h  10000
1i  blank
1j  checked
1k  0
1l  United States
1m  03/01/2025
1n  blank
1o  United States
2   checked
3   checked

Part II
4a  San Zhang
    No. 88 Renmin Road, Dali, Yunnan, China
4b(1) blank
4b(2) blank
4b(3) blank
4c  China
4d  China
4e  China

Part III
Foreign person: checked
8a  San Zhang
    No. 88 Renmin Road, Dali, Yunnan, China
8b(1) blank
8b(2) blank
8b(3) blank
8c  Individual Investor
8d  blank
8e  Related to reporting corporation: checked
    Related to 25% foreign shareholder: blank
    25% foreign shareholder: checked
8f  China
8g  China

Part IV
9–36 all blank or 0

Part V
checked

Part VI
blank

Part VII
37 No
38a No
39 No
40a No
41a No
42 No
43 No
```

```Plain Text
PART V ATTACHMENT

Reporting Corporation: MTPARK LLC
EIN: 12-3456789
Tax Year: 01/01/2025 – 12/31/2025

1. On March 5, 2025, the sole foreign owner, San Zhang, made a capital contribution of USD 10,000 to MTPARK LLC in connection with the funding of the entity.
```

```Plain Text
PRO FORMA FORM 1120

Write across top: Foreign-owned U.S. DE

Name: MTPARK LLC
Address: 8 The Green, Suite A, Dover, DE 19901, USA
B. EIN: 12-3456789
C. Date incorporated: 03/01/2025
D. Total assets: 10000
E. Check if: Initial return

All other lines blank
```
