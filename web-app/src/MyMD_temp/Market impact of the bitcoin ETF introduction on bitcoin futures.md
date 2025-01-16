International Review of Financial Analysis 97 (2025) 103810

Contents lists available at ScienceDirect

International Review of Financial Analysis

journal homepage: www.elsevier.com/locate/irfa

Market impact of the bitcoin ETF introduction on bitcoin futures

Yu-Lun Chen a,*, Ke Xu b, J. Jimmy Yang c
a Department of Finance, College of Business, Chung Yuan Christian University, Taiwan
b Department of Economics, University of Victoria, Canada
c School of Accounting, Finance, and Information Systems, College of Business, Oregon State University, United States

A R T I C L E I N F O

A B S T R A C T

JEL Classification:
G10
G14
G20

Keywords:
Bitcoin futures
ProShares bitcoin strategy ETF (BITO)
Efficiency
Liquidity

1. Introduction

We investigate the introduction effect of ProShares bitcoin strategy ETF (BITO) on investor structure and market
quality in Chicago Mercantile Exchange bitcoin futures. We find that the BITO introduction significantly changes
the investor structure in bitcoin futures, with ETF asset managers being the major long-side participants against
the short-side hedge funds. Furthermore, market participants become more concentrated and the market
liquidity improves in the bitcoin futures after the BITO introduction. The change in investor structure hurts
futures’ price efficiency during the first three days of BITO introduction, but it then returns to the normal level.
The BITO introduction does not appear to affect long-run market efficiency and volatility of bitcoin futures.

Bitcoin is the first and most famous cryptocurrency. The first US
bitcoin exchange-traded fund (ETF), “BITO”, issued by ProShares, began
trading on October 19, 2021. BITO holds bitcoin futures contracts rather
than the spot bitcoin. According to the Hajric (2021), BITO is the second-
most heavily traded fund on its debut day on record, with more than 24
million shares changed hands. In August 2021, the Securities and Ex-
change Commission (SEC) Chairman Gary Gensler expressed a prefer-
ence for ETFs that hold bitcoin futures because they are traded on
regulated venues such as the Chicago Mercantile Exchange (CME).1 Spot
bitcoin, on the contrary, is predominantly traded on non-regulated ex-
changes and large bitcoin price dispersions exist among these exchanges
(Makarov & Schoar, 2020Cong et al., 2023). However, the futures-based

BITO may be subject to potentially larger tracking errors and the
occurrence of the futures rolling cost.2 In addition, the introduction of
BITO may affect market liquidity, volatility, and price efficiency in the
underlying bitcoin futures market, which has not been explored. We
attempt to fill this gap in the literature.

Bitcoin market is notoriously volatile, far from being efficient, and
with high information asymmetry (Makarov & Schoar, 2020 Tiniç et al.,
2022) but is still attractive to many investors. CME’s bitcoin futures, a
USD cash-settled contract, gives investors exposure to bitcoin without
having to hold spot bitcoin. In addition, bitcoin futures market provides
investors with higher trading transparency, better price discovery, and
hedging opportunities (Kapar & Olmo, 2019 Wu et al., 2021).3 If the
introduction of futures-based BITO affects market liquidity, volatility,
and price efficiency in bitcoin futures, these impacts may spill over to

* Corresponding author at: 200 Chung Pei Rd., Jhongli, Taoyuan 32023, Taiwan.

E-mail addresses: yoloom@cycu.edu.tw (Y.-L. Chen), kexu@uvic.ca (K. Xu), Jimmy.Yang@bus.oregonstate.edu (J.J. Yang).

1 The U.S. SEC has approved 11 spot bitcoin ETFs and their trading began on January 11, 2024. The SEC stated that bitcoin is primarily a speculative, volatile asset
that’s also used for illicit activity including ransomware, money laundering, sanction evasion, and terrorist financing. While the SEC approved the listing and trading
of certain spot bitcoin exchange-traded products, the SEC did not approve or endorse bitcoin. Spot trading in bitcoin takes place on a broad variety of largely
unregulated exchanges.

2 BITO needs to roll the CME bitcoin futures contract, which means BITO issuer will sell the near futures contract it holds and buy a contract with a later expiration
date, when the futures contract is nearing expiration. Rolling bitcoin futures contracts will regularly incur some costs for BITO. In addition, BITO invests in bitcoin
futures and may assume the tracking errors. Thus, BITO may not fully capture the performance of spot bitcoin.

3 Kapar and Olmo (2019) and Wu et al., 2021 find that bitcoin futures market dominates the spot market in the price discovery process.

https://doi.org/10.1016/j.irfa.2024.103810
Received 27 February 2024; Received in revised form 3 November 2024; Accepted 19 November 2024
Available online 22 November 2024
1057-5219/© 2024 Elsevier Inc. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

Y.-L. Chen et al.

International Review of Financial Analysis 97 (2025) 103810

the spot bitcoin prices across exchanges and affect price integration
among these exchanges.4

In this research, we investigate how the introduction of BITO affects
the market quality of bitcoin futures and the trading positions of various
types of traders.5 While the impact of ETF introductions on market
quality has been extensively studied (Park & Switzer, 1995 Ackert &
Tian, 1998 Switzer et al., 2000 Ackert & Tian, 2001 Kurov & Lasser,
2002 Hegde & McDermott, 2004 Israeli et al., 2017 Glosten et al., 2021
Box et al., 2021), these empirical investigations have primarily focused
on equity ETFs such as SPDRS, QQQ, and DIAMONDS. BITO, however, is
different because it holds futures contracts instead of spot or physical
assets. The higher volatility and asymmetric information in the bitcoin
market may lead to a unique market shock from BITO’s introduction
compared to equity ETFs. This study specifically examines changes in
the investor structure, highlighting the roles of ETF asset managers and
hedge funds post-BITO introduction, to provide a nuanced understand-
ing of its market impact.

Makarov and Schoar (2020) find that order flow explains about 85 %
of returns in the cryptocurrency market, compared with about 15 %–30
% in stock or treasury markets and up to 50 % in foreign exchange
markets. The strong relation between order flow and returns highlights
the high asymmetric information or inventory-holding cost in the
cryptocurrency market. Many investors may face a lack of sufficient
information about what bitcoin is and how it works (Zhang et al.,
2023).6 In addition, the history of cryptocurrency is marked by
numerous hack attacks and thefts, and it is heavily influenced by
investor attention and sentiment (Zhu et al., 2021). Hence, investors
may feel uncomfortable trading spot bitcoin in unregulated exchanges
directly and turn to bitcoin ETFs in the regulated environment for se-
curity reasons. The BITO introduction may transfer the bitcoin demand
of retail investors into bitcoin futures, which should be reflected on BITO
asset managers’ trading positions in bitcoin futures and affect the mar-
ket liquidity of bitcoin futures.

Fig. 1 plots the time-varying bitcoin futures prices and open interest.
It is noticeable that the futures prices and open interest rise substantially
after March 17, 2020 (COVID-19 pandemic and the U.S. Federal Reserve
stimulus program shocks), as shown in the first dashed vertical line.7
More importantly, after the second dashed vertical line (Oct. 19, 2021,
the introduction date of BITO), the open interest spiked initially and
then gradually decreased along with the bitcoin futures price. This figure
supports that the introduction of BITO attracts more trading in the

4 Makarov and Schoar (2020) point out that, in the cryptocurrency market,
there are many nonintegrated exchanges that are independently owned and
exist in parallel across countries. They show the amount of price dispersion and
arbitrage profit between these exchanges, suggesting that the cryptocurrency
market is far from efficient. In addition, Augustin et al. (2023) find that the
introduction of bitcoin futures is beneficial to the bitcoin spot market by
making the underlying prices more informative.

5 Market quality refers to a market’s ability to meet its dual goals of liquidity

and price discovery (O’Hara & Ye, 2011).

6 Zhang et al. (2023) find that most bitcoin participants are actually new to
the blockchain technology. Therefore, the Plus Token Ponzi scheme was able to
easily fool these participants with their key white paper marketing claims.

7 The U.S. Federal Reserve announced its full range of tools (LSAPs) to sup-
port households, businesses, and the overall U.S. economy against the coro-
navirus pandemic on March 23, 2020. For example, the FOMC decided to
purchase Treasury securities and agency mortgage-backed securities in the
amount needed to support smooth market functioning and effective trans-
mission of monetary policy to broader financial conditions and the economy.

bitcoin futures. In addition, Fig. 2 plots the time-varying bitcoin futures
return volatility and shows that the largest volatility jump occurred on
March 17, 2020 (the first dashed vertical line), but there are no obvious
changes in volatility after the BITO introduction. The second and third
largest jumps of futures volatility occurred in January and May of 2021.8
BITO introduction does not seem to increase bitcoin futures volatility.
Our research is underpinned by the market microstructure literature,
which provides insights into how the introduction of BITO ETF may
influence market liquidity, efficiency, and volatility (Switzer et al., 2000
Kurov & Lasser, 2002 Ben-David et al., 2018 O’Hara, 2020). According
to these studies, the introduction of an ETF can impact market partici-
pants and subsequently alter trading dynamics and market quality
metrics. Ben-David et al. (2018) further explore the liquidity trading
hypothesis and price discovery hypothesis to illustrate the impact of ETF
trading on the prices of underlying securities. Additionally, we consider
theories of investor behavior to analyze how different types of investors,
specifically ETF asset managers and hedge funds (Chen & Yang, 2021),
contribute to changes in market structure and quality.

To explore changes in the market quality of CME bitcoin futures, we
use high-frequency trading data of bitcoin futures to measure the time-
varying liquidity, realized volatility, Hasbrouck (1993) pricing error,
and variance ratio. In addition, we adopt the Traders in Financial Fu-
tures (TFF) report from the U.S. Commodity Futures Trading Commis-
sion (CFTC) to classify traders into five categories, including asset
managers, dealers, leveraged funds, other reportable traders, and non-
reportable traders, in the bitcoin futures market.

Our analysis yields some interesting results. First, we find compelling
new evidence on the changes of trader structure in bitcoin futures after
the BITO introduction. Leveraged funds (i.e., hedge funds) play an
important role in the bitcoin futures market as, before the introduction
of BITO, they exhibit the highest participation rate on both long and
short sides. Especially, their trading position on the short side ranged
from 50 %–80 %. After the BITO introduction, the trading position of
ETF asset managers on the long side increases dramatically from 8 % to
about 50 %, making them the major long-side participants against the
short-side leveraged funds. Dealers (or large banks) who serve as market
makers in the market play a rather small role in bitcoin futures, unlike
their participation in other futures markets. We also find that the per-
centage of long positions held by the largest four (eight) traders in-
creases from 30 % to 60 % (50 % to 70 %) after the introduction of BITO,
suggesting that the bitcoin futures market becomes more concentrated
on fewer institutional traders. Market concentration is apparently higher
in bitcoin futures than in equity index, bond, and other commodity
futures.

Second, to check whether the BITO introduction alters dynamic
trading interactions among the different types of traders in bitcoin fu-
tures, we employ the Diebold and Yilmaz (2012 and 2014) method and
TVP-VAR method (Antonakakis et al., 2020) to examine the trading
spillovers among these traders. The results of Diebold and Yilmaz and
TVP-VAR spillover methods show that leveraged funds play the major
transmitter role in trading spillover to others, while asset managers are
the major recipients. However, the BITO introduction increases the
magnitude of asset managers’ trading against leveraged funds. It is
plausible that the increased long positions of asset managers after the
BITO introduction may entice leveraged funds to bet against them and
take more short positions in bitcoin futures.

Third, for market quality, we find that market liquidity of the bitcoin

8 According to CNBC news on January 29, 2021, Tesla CEO Elon Musk added
the phrase “#bitcoin” to his Twitter bio, alongside a cryptic tweet reading: “In
retrospect, it was inevitable.” In the immediate aftermath of this simple signal
of Musk’s attention, the valuation of bitcoin shot up 20 %. According to CNN
Business on May 13, 2021, the price of bitcoin has nosedived after Musk said his
company was suspending plans to accept the cryptocurrency as payment for
electric vehicles.

2

Y.-L. Chen et al.

International Review of Financial Analysis 97 (2025) 103810

Fig. 1. CME bitcoin futures prices and its open interest.
Note: The first dashed vertical line indicates on March 17, 2020 and the second dashed vertical line indicates the introduction day of BITO (10/19/2021).

Fig. 2. CME bitcoin futures return volatility.
Note: The first dashed vertical line indicates on March 17, 2020 and the second dashed vertical line indicates the introduction day of BITO (10/19/2021). Return
volatility is measured by the standard deviation of one-, five-, and twenty- minutes bitcoin futures return on a weekly basis.

futures improves while efficiency and volatility remain unchanged after
the BITO introduction. The improved liquidity can be a result of the
BITO fund inflow from the demand of retail traders to take long positions
in bitcoin futures indirectly through BITO, leading to the increased
trading positions of asset managers in bitcoin futures. Since retail traders
are essentially analogous to “uninformed traders”, their increased
participation in bitcoin futures through BITO may attract leveraged
funds to take advantage of their uninformed trades. Baur and Smales
(2022) find that leveraged funds play a key role in the bitcoin futures
market (“smart money”) and display better market timing ability
(“informed traders”). Hence, both uninformed and informed traders
may increase their positions after the BITO introduction, enhancing the

bitcoin futures market liquidity but having insignificant impact on the
market efficiency. In addition, the BITO introduction does not increase
the volatility of bitcoin futures, which differs from the finding of Ben-
David et al. (2018) on equity ETFs.

Fourth, to better understand the BITO effect, we analyze the
liquidity, volatility, and price efficiency in bitcoin futures at a daily
frequency around the BITO introduction day. About $1.2 billion flowed
into BITO during its first three days on the market, according to the
statistics of ETF.com database. Thus, we focus on short-term liquidity,
volatility, informed trading, and price efficiency in bitcoin futures dur-
ing the five trading days before and after the BITO introduction. We find
that fund inflow of BITO enhanced the liquidity in bitcoin futures during

3

Y.-L. Chen et al.

International Review of Financial Analysis 97 (2025) 103810

the first five days. However, the BITO introduction hurts bitcoin futures’
price efficiency on the first three days, but the efficiency reverts back to
the normal level soon after.

We contribute to the literature in several ways. First, we investigate
the impact of BITO introduction on investor structure in bitcoin futures.
We document the small role of dealers, the closely related trading
interaction between asset managers and leveraged funds, and the
extremely high market concentration in bitcoin futures, which differ
from other futures markets. Second, this is the first work to provide
empirical evidence of the BITO introduction effect on market quality of
the underlying bitcoin futures. In addition, we also check the intro-
duction of the ProShares Bitcoin Short ETF (BITI) and find insignificant
impact on market quality of bitcoin futures.9 Finally, we find that BITO
trading may affect bitcoin futures’ price efficiency, but the impact is
short-lived. Makarov and Schoar (2020) argue that cryptocurrencies are
still at their early stage in the finance and economics literature. Hope-
fully, our work will inspire more studies to investigate the effects of
bitcoin ETFs on the bitcoin spot and derivative markets to enhance our
understanding of cryptocurrencies.

The remainder of this paper is organized as follows. We review the
previous ETFs literature and pose the research hypotheses in Section 2
and 3, followed by Section 4 of data description and trading position
analysis. We analyze the impact of BITO introduction on trading posi-
tion spillover in bitcoin futures in Section 5 and market quality in Sec-
tion 6. We analyze the short-term market quality around the BITO
introduction in Section 7. Finally, we present the conclusions drawn
from this study in Section 8.

2. Literature review

Understanding the market impact of ETFs trading is crucial for aca-
demic researchers, policymakers, and investors, so a rich literature has
investigated the effect of equity ETFs trading on index futures, index
options, and the underlying stocks (Park & Switzer, 1995 Ackert & Tian,
1998 Switzer et al., 2000 Ackert & Tian, 2001 Kurov & Lasser, 2002
Hegde & McDermott, 2004 Israeli et al., 2017 Glosten et al., 2021 Box
et al., 2021). We separate these studies into two branches: 1) exploring
the impact of equity ETFs introduction on the underlying derivative
market and 2) exploring the impact of equity ETFs trading on the un-
derlying stocks.

In the first line of research, Park and Switzer (1995) find that the
introduction of Toronto 35 Index Participation Units (TIPs) enhances the
price efficiency of Toronto 35 index futures and Ackert and Tian (1998)
find similar result for Toronto 35 index options. Switzer et al. (2000) and
Chu and Hsieh (2002) find that S&P 500 index futures’ pricing efficiency
enhances after the introduction of Standard and Poor’s Depository Re-
ceipts (SPDRs). Ackert and Tian (2001) also find similar result for S&P
500 index options. Additionally, Kurov and Lasser (2002) find that
Nasdaq-100 index futures’ pricing efficiency improves after the intro-
duction of QQQ. These studies argue that equity ETFs allow investors to
track the performance of stock portfolios efficiently, avoid the short-sale
constraint, and incur lower transaction cost. Therefore, equity ETFs
provide better engagement in index arbitrage with index futures or
options, leading to their improved price efficiency.

In the second line of research, researchers focus on ETFs trading and
their underlying stocks’ liquidity, volatility, and pricing efficiency.
Hegde and McDermott (2004) find the liquidity of the Dow Jones In-
dustrial Average 30 (NASDAQ 100) index component stocks improves
after the introduction of the DIAMONDS (QQQ), largely because of a

9 Nowadays, there are several bitcoin ETFs which invest Bitcoin futures
contracts and the largest assets under management (AUM) of these ETFs is BITO
(about $ 1.1 billion USD), followed by BITI (about $ 70 million USD). Relatively
smaller AUM of BITI or other bitcoin ETFs may have caused their insignificant
impact on bitcoin futures.

4

decline in the adverse selection cost of the underlying stocks. Israeli
et al. (2017) find that an increase in ETF ownership is accompanied by a
decline in pricing efficiency for the underlying stocks. Ben-David et al.
(2018) argue that, due to equity ETFs’ low trading costs, ETFs could
attract short-horizon liquidity traders and the liquidity shocks can
propagate to the underlying stocks through the arbitrage channel (i.e.,
the creation and redemption).10 Then, the arbitrage trading of ETFs may
increase the non-fundamental volatility of the underlying stocks and
have no effect on the pricing efficiency. By contrast, Glosten et al. (2021)
find the greater ETF trading is associated with improvement in short-run
informational efficiency for the underlying stocks. Box et al. (2021) find
little support that ETFs trading transmits noise to the underlying stocks
and present strong evidence that ETF prices are more likely to follow the
underlying stock returns. They find, rather than transmitting non-
fundamental shocks, ETFs trading would improve the liquidity of the
underlying stocks.

In sum, these studies support that ETFs trading improves the
liquidity of their underlying stocks, but the effect of ETFs trading on
pricing efficiency of the underlying stocks is not well settled in the
literature. Some argue that ETFs trading enhances pricing efficiency of
the underlying stocks (Hegde & McDermott, 2004 Glosten et al., 2021),
while others reveal that ETFs noise trading do not improve pricing ef-
ficiency of the underlying stocks (Israeli et al., 2017 Ben-David et al.,
2018).

3. Research hypotheses

Besides the equity ETFs, some studies focus on market impact of VIX
index, bond, and commodity ETFs (Zhang, 2015 Chen & Yang, 2021
Todorov, 2021a). Chen and Yang (2021) find that, after the introduction
of VIX exchange-traded products (ETPs), large-scale hedging activities
of ETPs issuers drive the underlying VIX futures prices away from their
equilibrium level. Todorov (2021a) argues that the creation and
redemption mechanism, which keeps bond ETFs prices aligned with the
NAV of the underlying bonds, operates differently from that of equity
ETFs. This difference makes it harder for arbitrageurs to exploit price
gaps and impacts ETFs premium and tracking errors in stress times.
Zhang (2015) shows that, after the introduction of gold ETF (GLD), the
liquidity of gold company stocks declined and their adverse-selection
risk increased. Da et al. (2023) find that commodity ETF arbitrage, as
a specific form of index trading, can inject unrelated noise into futures
prices and diminish price efficiency.

The VIX, bond, and commodity ETFs have some different properties
than equity ETFs (i.e., SPDRs, QQQ, and DIAMONDS). (1) It may be
difficult to execute the creation and redemption arbitrage for some of
those ETFs, so they need an arbitrage mechanism to keep their share
prices aligned with the NAV, especially in the stress times. Hence, some
previous studies focus on the ETFs premium/discount or tracking error.
(2) Some of the underlying spot assets are difficult to be stored (i.e.,
energy commodities) or traded (i.e., VIX), so those ETFs issuers would
use the related futures contracts to track the performance of these un-
derlying assets. Since those trading of ETFs issuers may directly affect
the market quality in the related futures, the shock of those ETFs would
be different from the market impact of equity ETFs (Park & Switzer,
1995 Ackert & Tian, 1998 Switzer et al., 2000 Ackert & Tian, 2001
Kurov & Lasser, 2002).

10 ETFs are traded in the secondary market but ETF shares can be created and
redeemed in the primary market. When the secondary market price of ETF
diverges from the value of the underlying securities (i.e., net asset value, NAV),
arbitrageurs can create new ETF shares by buying the underlying securities of
the ETF and transferring them to the ETF sponsor. Similarly, arbitrageurs can
redeem ETF shares and receive the underlying securities of the ETF. Through
the creation and redemption, the secondary market price of ETF would move
close to the NAV of ETF.

Y.-L. Chen et al.

International Review of Financial Analysis 97 (2025) 103810

BITO clearly belongs to the futures-based ETF category, so its
structure is also different from equity ETFs. Essentially, BITO framework
is similar to that of commodity or VIX ETFs (Todorov, 2021b). There-
fore, we first hypothesize that the trading of futures-based BITO would
impact market liquidity, volatility, and pricing efficiency in the under-
lying bitcoin futures. Additionally, the fund inflow of BITO may corre-
spond to positions held by ETF asset managers in bitcoin futures.
Subsequently, other institutional investors would interact with ETF asset
managers’ positions and engage in trading in the bitcoin futures. Thus,
our second hypothesis posits that the introduction of BITO would in-
fluence trading transmissions among major types of traders in the bit-
coin futures. Investigating the impact of BITO introduction on the
investor structure and market quality of bitcoin futures will provide new
insights in the literature on ETFs and cryptocurrencies.11

4. Data and trading position analysis

We illustrate the CME bitcoin futures data, the TFF report, descrip-
tive statistics of these data, and trading position analysis in this section.

4.1. CME bitcoin futures data

We collect the intra-day trading data of CME bitcoin futures from
Tick Data, Inc. for the period of January 1, 2018 to October 31, 2022.
Although both the Chicago Board Options Exchange (CBOE) and CME
launched Bitcoin futures in December 2017, Hung et al. (2021) find that
CME’s bitcoin futures exhibit superior price discovery than CBOE’s.
Since the CBOE delisted all the bitcoin future derivatives from its futures
market in June 2019, we only focus on CME bitcoin futures (ticker
symbol BTC), which is a USD cash-settled contract based on the CME CF
Bitcoin Reference Rate (BRR) that serves as a once-a-day reference rate
of the U.S. dollar price of bitcoin. We provide detailed contract speci-
fications for the CME bitcoin futures in Appendix A. For our empirical
analyses, we use the prices of the most actively traded nearest-to-
maturity futures contracts.

To analyze the market quality of bitcoin futures, we focus on three
different aspects: (1) liquidity, (2) volatility, and (3) price efficiency. We
employ various methods to measure these aspects, utilizing different
frequencies of intra-day bitcoin futures data. Specifically, we use one-
minute, five-minute, and twenty-minute bitcoin futures returns over a
week to calculate realized variances. This approach follows Andersen
et al. (2001) and Andersen et al. (2003), who use five-minute returns to
compute weekly realized volatility. For the pricing error measurement
(Hasbrouck, 1993), we use one-minute bitcoin futures returns over a
week, following Chen and Xu (2021). We analyze variance ratios by
adopting one-minute, five-minute, twenty-minute, and one-hour bitcoin

11 Our paper differs from the existing literature in several crucial ways: (1)
Asset Class and Instrument Focus: While much of the existing research focuses
on equity ETFs and their impact on traditional financial instruments such as
index futures and options, our study is among the first to examine a bitcoin
futures ETF and its effect on the underlying bitcoin futures market. This pro-
vides novel insights into the rapidly evolving cryptocurrency markets. (2)
Investor Structure Analysis: Our study delves deeply into the changes in the
investor structure, specifically highlighting the roles of ETF asset managers and
hedge funds. This detailed analysis of market participants provides a nuanced
understanding of how the introduction of a bitcoin futures ETF reshapes the
market landscape. (3) Short-term vs. Long-term Effects: We differentiate be-
tween the short-term disruption in price efficiency observed in the first three
days post-BITO introduction and the long-term effects, where the market effi-
ciency and volatility return to normal levels. This temporal analysis offers a
more comprehensive view of the ETF’s impact, which is often not addressed in
the equity ETF literature. (4) Specific Market Dynamics: Our findings highlight
the concentration of market participants and the implications for market
quality and liquidity, providing unique insights into how these dynamics play
out in the context of bitcoin futures.

futures price data, in line with Boehmer and Kelley (2009). The choice of
frequency is determined by the need to capture short-term market dy-
namics and effectively avoid microstructure noise in bitcoin futures
prices, as supported by related previous studies.

4.2. Traders in financial futures (TFF) report and trading positions

The CFTC publishes weekly TFF reports to add transparency to the
financial futures markets, in addition to the legacy ‘Commitments of
Traders’ (COT) report. The TFF reports of bitcoin futures are available
going back to April 10, 2018, so we focus on the sample period from
April 10, 2018 to October 31, 2022 in this study. The TFF report clas-
sifies large traders in the bitcoin futures into four reportable categories,
including (1) asset managers/institutional
traders, (2) dealers/in-
termediaries, (3) leveraged funds, and (4) other- reportable traders.
Large traders in all four categories of the TFF report may be drawn from
either the commercial or non-commercial categories of traders in the
traditional COT report.

TFF reports provide a breakdown of open interest positions held by
traders on each Tuesday for futures markets. According to the explan-
atory notes on the TFF reports (obtained from the CFTC website), all
financial futures market participants are divided into sell and buy sides,
with the category entitled “dealers” representing sell-side participants.
Typically, these market participants are dealers and intermediaries
earning commission on the sale of financial products, capturing bid/
offer spreads and accommodating the needs of their clients. This cate-
gory includes large banks (U.S. and non-U.S.) as well as dealers in se-
curities, swaps and other derivatives.

The three remaining categories represent buy-side participants. All
of them are essentially the clients of the sell-side participants and use the
futures contracts to invest, hedge, or speculate. “Asset managers”
include ETFs asset managers, insurance firms, mutual fund managers,
and all portfolio/investment managers whose clients are predominantly
institutional investors. “Leveraged funds” typically comprise hedge
funds and various types of money managers, including registered com-
modity trading advisors, registered commodity pool operators, and
unregistered fund managers identified by the CFTC. The strategies
adopted by these traders may involve taking outright positions or
arbitrage within and across markets. They may also be engaged in
managing and conducting proprietary futures trading and trading on
behalf of speculative clients. Any traders who do not belong to one of the
above categories fall into the category of “other reportable traders”,
including corporate treasuries, central banks, smaller banks, mortgage
originators, credit unions, and any other reportable traders not assigned
to the other three categories.

The TFF reports disclose open interest positions, both long and short,
of these four categories of traders and non-reportable traders. In addi-
tion, it discloses the concentration ratio of reportable long and short
positions for the largest four and eight traders’ open interests. We
construct two trading position measures for these categories of traders to
proxy their trading activities: (1) Percentage trading positions (PTPi
t)
t) held by type i, where i = AS, DE, LE,
and (2) Net trading positions (NTPi
OT, and NO, which respectively refer to asset managers, dealers,
leveraged funds, other-reportable traders, and non-reportable traders.
Both measures are defined as follows:

PTPi
t

=

(
Longi
t

+ Shorti
t

+ 2 • Spreadingi
t

MTOIt

)/

NTPi
t

= Longi
t

(cid:0) Shorti
t

,

(1)

(2)

t and Shorti

where Longi
t refer to the long and short positions held by type i
traders on t. MTOIt is the market’s total open interest. Spreadingi
t mea-
sures the extent to which type i traders hold equal long and short futures
positions. PTPi
t measures the participation ratio of type i traders in the
whole market, regardless of their standing on long- or short- sides, while

5

Y.-L. Chen et al.

International Review of Financial Analysis 97 (2025) 103810

NTPi

t measures the net long trading position of the type i traders.

4.3. Trading position analysis before and after BITO introduction

To analyze whether the trader positions in bitcoin futures are
affected by the BITO introduction, we plot the long and short trading
position percentage of different types of traders against the total position
in Fig. 3. Leveraged funds have the highest participation proportion on
both long and short sides (i.e., dark red line), with their percentages on
the short side ranging from 50 % to 80 %. In Fig. 3.1, after the intro-
duction of BITO (i.e., the dashed vertical line), the trading percentage of
asset manager on the long side increases dramatically from 8 % to about
50 % (i.e., dark blue line). In Fig. 3.2, after the introduction of BITO, the
trading percentages of all traders on the short side do not seem to exhibit
noticeable changes. Fig. 3 shows that asset managers become the major
long-side participants against the short-side leveraged funds after the
BITO introduction.

Then, we plot percentages of long and short open interest held by the
largest four and eight traders against total open interest (market con-
centration) in Fig. 4. We find the blue line in Fig. 4.1 rises significantly
after the dashed vertical line, showing that the percentage of long po-
sitions held by the largest four traders increases from 30 % to 60 %
across the BITO introduction. For the red line, we find the percentage of
short positions held by the largest four traders decreases slightly. In
Fig. 4.2, for the percentages of long and short open interest held by the
largest eight traders, we find a similar pattern to Fig. 4.1. Overall, Fig. 4
shows that the bitcoin futures market becomes more concentrated on the
long side after the introduction of BITO. The market concentration of
bitcoin futures is apparently higher than those in equity index, bond,
and commodity futures.

To check whether the increased trading percentage of asset managers
on the long side comes from the BITO trading and induces high market
concentration of largest four traders, we plot the net-long position of
asset managers (i.e., the blue line), the market concentration of the
largest four traders (i.e., the green line), and the accumulated fund flow
of BITO (i.e., the red line) in Fig. 5. Major fund inflow of BITO con-
centrates on the first three days of BITO introduction and then gradually
increases to a stable level. These variable series all jump on the BITO
introduction day and co-move together. In addition, we find that the
pairwise correlation coefficient between the net-long position of asset
managers (the market concentration of the largest four traders on long
positions) and the accumulated fund flow of BITO is about 0.80 (0.85).
These findings in Fig. 5 confirm that fund inflow of BITO increases the
long position of asset managers and market concentration in bitcoin
futures.

In Table 1, we present the summary statistics of bitcoin futures re-
turn, percentage trading positions (PTPi
t), and net trading positions
(NTPi
t) for the entire sample period (Panel A) and the two sub-periods
separated by the BITO introduction (before in Panel B and after in
Panel C). We also test the hypotheses on the equality of bitcoin futures
return, PTPi
t in the two sub-periods and present results in
Panel D.

t, and NTPi

Panel A of Table 1 shows that leveraged funds take more positions in
bitcoin futures than others, with an average trading percentage of about
55.1 %. Leveraged funds are major net-short traders, whereas asset
managers and non-reportable traders hold net-long positions. In Panels
B and C of Table 1, we find that on average, the trading percentage of
asset managers increases from 4.28 % to 28.12 % and their net-long
position increases from 53.7 to 5032.4, a level near the net-short posi-
tion of leveraged funds. This result implies that the increased long po-
sitions of asset managers after the BITO introduction are mostly matched
by the increased short positions of leveraged funds from (cid:0) 1643.6 to
(cid:0) 5334.3. That is, when asset managers increase their positions in bit-
coin futures because of BITO, leveraged funds stand to take the opposite
side of the transactions.

On the contrary, the trading percentage of non-reportable traders
decreases from 19.34 % to 9.05 % and their long position also drops
from 1262.4 to 479 after the BITO introduction. This finding supports
the conjecture that some retail traders may reduce their trading in bit-
coin futures and turn to BITO for their bitcoin exposure without the need
to deal with the contract expiration issue in futures. Lastly, in Panel D of
Table 1, we find that bitcoin futures return, PTPi
t all exhibit
significant changes after the BITO introduction. These results suggest
that the BITO introduction alters trader positions and investor structure
in bitcoin futures.

t, and NTPi

5. Analysis of trading position spillover in CME bitcoin futures

To further understand the intertemporal trading interactions among
different types of traders in bitcoin futures, especially from the BITO
shock, we use the spillover measure of Diebold and Yilmaz (2012 and
2014) and of TVP-VAR methodology (Antonakakis et al., 2020) to
examine the trading spillovers among these traders. The Diebold and
Yilmaz (2012 and 2014) measurement is well established for examining
return or volatility spillover transmissions or network connectedness in
various financial markets. For instance, Ji et al. (2019) adopt the same
measure to analyze trading position spillover transmissions in futures
markets. Likewise, we employ the vector autoregression (VAR) model
t), where i = AS, DE, LE,
for the changes in net trading positions (ΔNTPi
OT, and NO, which respectively refer to asset managers, dealers,
leveraged funds, other-reportable traders, and non-reportable traders.12
However, rolling-window VAR-based dynamic spillover measures is
sensitive to the window size choices, besides the initial loss of obser-
vations equal to the window size. Antonakakis et al. (2020), point out
that the advantages of the TVP-VAR spillover model include: (1) no need
to arbitrarily set the rolling-window size, (2) no loss of observations, and
(3) no outlier sensitivity. Hence, we consider both TVP-VAR-based and
rolling-window VAR-based dynamic spillover measures in this study.

Here, we illustrate the TVP-VAR(p) model and estimate a TVP-VAR
model with one lag (p = 1) as suggested by the Bayesian information
criterion (BIC) as follows:

Yt = βtYt(cid:0) 1 + εt, where εt ∼

(cid:0)

)

0, Σ1,t

vec(βt

) = vec(βt(cid:0) 1

) + vt, where vt ∼

(cid:0)

)

0, Σ2,t

(3)

(4)

where Yt represents a m × 1 net trading positions changes (ΔNTPt)
vector, βt is a m × m dimensional coefficient matrix and εt is a m × 1
dimensional error disturbance vector with a m × m variance-covariance
matrix, Σ1,t. vec(βt
) and vt denote m2 × 1 dimensional vectors. Moreover,
Σ2,t. is a m2 × m2 variance-covariance matrix.

In order to calculate the generalized impulse response functions
(GIRF) and generalized forecast error variance decompositions
(GFEVD), we transform the TVP-VAR to its vector moving average
(VMA) representation based on the Wold representation theorem, ac-
cording to Antonakakis et al. (2020). VMA is as follows:

Yt =

∑∞

j=0

Bjtεt(cid:0) j,

(5)

where Bjt is an m × m dimensional matrix. The (scaled) GFEVD nor-
malizes the (unscaled) φg
(H), in order that each row sums up to uni-
ⅈj,t
ty. ̃φg
(H) represents the pairwise directional connectedness from j to i
ij,t
and illustrates the influence variable j has on variable i in terms of its
forecast error variance share. These variance shares are then

12 Due to the space constraint, please refer to the studies by Diebold and
Yilmaz (2012 and 2014) for a detailed explanation of this method and the
related measures.

6

Y.-L. Chen et al.

International Review of Financial Analysis 97 (2025) 103810

Fig. 3. Time-varying percent of different traders’ open interest against the total open interest.
Note: The dashed vertical line indicates the introduction day of BITO (10/19/2021).

normalized, so that each row sums up to one, meaning that all variables
together explain 100 % of variable i’s forecast error variance. This is
calculated as follows:

H stands for the forecast horizon.

Based on the GFEVD, Diebold & Yilmaz, 2012, Diebold & Yilmaz,
2014), and Antonakakis et al. (2020), we can construct the total trading
spillover (TS) index of all trading positions as follows:

φg
ⅈj,t

(H) =

∑H(cid:0) 1

(cid:0)

σ(cid:0) 1
jj,t

t=1
(cid:0)
∑H(cid:0) 1

∑m

j=1

t=1

)

2

ʹ
iBtΣ1,tej
e

ʹ
ʹ
iBtΣ1,tB
e
tei

, ̃φg
ij,t
)

(H) =

(H)

φg
ij,t
∑m

φg
ij,t

(H)

j=1

̃φg
ij

(H) =

φg
ij
∑N

(H)

.
(H)

φg
ij

j=1

(6)

TSt(H) =

∑m

i,j=1

i∕=j
∑m

i,j=1

̃φg
ij

(H)

• 100.

̃φg
ij

(H)

(7)

∑

∑

m
j=1

̃φg
ij,t

(H) = 1 and

̃φg
(H) = m. In addition, σjj is the
with
ij,t
standard deviation of the error term for the jth equation; ei (ej) is the
selection vector, with one being the ith (jth) element and zero otherwise.

m
i,j=1

Furthermore, we employ two spillover measurements, including the
net directional spillover (NDSi) and net pairwise directional spillover

7

Y.-L. Chen et al.

International Review of Financial Analysis 97 (2025) 103810

Fig. 4. Time-varying percent of open interest held by the largest four and eight reportable traders.
Note: The dashed vertical line indicates the introduction day of BITO (10/19/2021). We show the percent of open interest held by the largest four and eight
reportable traders (market concentration), without regard to whether they are classified as dealer, asset managers, or etc.

(NPDSij) in the Diebold and Yilmaz method and Antonakakis et al.
(2020). NDSi captures the directional spillover of trading positions from
type i traders to other types and from other traders to type i trader. A
positive (negative) NDSi indicates that the trading position of type i
trader represents a transmitter (receiver) in the whole market. Similarly,
NPDSij captures the pairwise directional spillover of trading positions
from type j to type i traders. A positive (negative) NPDSij indicates that
the trading position of type j(i) transmits information to the trading
position of type i (j).

The results of static trading spillovers of the TVP-VAR based measure

are presented in Table 2.13 The “net directional spillover” in NET row
shows that (1) Asset managers serve as the major receiver (Net direc-
tional spillover = 10.19 % - 18.15 % = (cid:0) 7.96 %); (2) Leveraged funds
serve as the major trading transmitters to others (Net directional spill-
over = 50.83 % - 42.85 % = 7.98 %), consistent with the findings of Ji
et al. (2019) that leveraged funds play a trading transmitter (spillover)
role in the futures market; (3) Dealers play a relatively small role in
trading interaction with others (Net directional spillover = 15.57 % -
17.30 % = (cid:0) 1.73 %).

Most importantly, we focus on the time variation in TVP-VAR-based

13 We thank an anonymous reviewer for suggesting the use of the TVP-VAR
model to conduct the trading position spillover analysis. The static and dy-
namic (rolling-window) analyses of the Diebold and Yılmaz (2012, 2014)
trading spillover measures are consistent with those obtained using the TVP-
VAR based measures. Due to space constraints, we do not report the results
of Diebold and Yılmaz (2012, 2014) trading spillovers here, but they are
available upon request.

8

Y.-L. Chen et al.

International Review of Financial Analysis 97 (2025) 103810

Fig. 5. Net-long position of asset managers, market concentration of the largest four traders on long position, and accumulated fund flow of BITO.
Note: In the sub-sample period (after the introduction day of BITO), the pairwise correlation coefficient between the net-long position of asset managers and the
accumulated fund flow of BITO is about 0.80. The pairwise correlation coefficient between the market concentration of the largest traders on long position and the
accumulated fund flow of BITO is about 0.85.

trading spillover measurements across all types of traders. Due to the
space constraint and the major participants being asset managers and
leveraged funds, we only plot time-varying NPDSij from leveraged funds
to asset managers in Fig. 6.14 It shows that, on average, leveraged funds
transmit more trading information to asset managers (i.e., Positive
NPDSij) than they receive from them. Obviously, NPDSij becomes smaller
after the dashed vertical line (the introduction day of BITO). Especially,
at the beginning of BITO introduction, asset managers suddenly trans-
form to information transmitters. This result indicates that the BITO
introduction alters dynamic trading interactions between asset man-
agers and leveraged funds in bitcoin futures. The increased trading po-
sition of asset managers from BITO trading may trigger leveraged funds

to also increase their participation by taking the opposite position dur-
ing the beginning of BITO introduction.

6. Market quality and trading positions in CME bitcoin futures

In this section, we investigate the impact of the BITO introduction on
market liquidity, volatility, and price efficiency in bitcoin futures.
Market liquidity and price discovery are the two most important func-
tions of financial markets and thus have naturally been a focus of
microstructure research (O’Hara, 2003). We explore the relation be-
tween net trading position and bitcoin futures return before and after the
BITO introduction, and then focus on the impact of BITO introduction on
market quality in CME bitcoin futures.

14 Due to space constraints, we do not report the results of dynamic NDS and
NPDS for other traders here, but they are available on request.

9

Y.-L. Chen et al.

International Review of Financial Analysis 97 (2025) 103810

Table 1
Summary statistics on the CME bitcoin futures return, percentage trading positions, and net trading positions.
This table reports the summary statistics of CME bitcoin futures return and the trading positions of the different types of traders over the full sample period (10 April
×
2018–31 October 2022) and the two sub-periods (before and after 19 October 2021). RB
t, which refer to the percentage trading positions held by type i traders on t, where i = AS, DE, LE, OT, and NO, which respectively refer to asset managers,
100. PTPi
(
=
dealers, leveraged funds, other-reportable traders, and non-reportable traders. PTPi
Longi
t refer to the
t
t
long and short positions held by type i traders on t, MTOIt is the market’s total open interest, and Spreadingi
and short futures positions. NTPi
standard deviation, skewness, and kurtosis of the time series. ***, **, and * indicate significance at the 1 %, 5 %, and 10 % levels, respectively.

t measures the extent to which type i traders holds equal long
t. Std. Dev., Skew., and Kurt. refer to the

t, which refer to the net trading positions held by type i traders on t; NTPi
t

t represent the return of CME bitcoin futures (time 100) on t; RB
t

)
/MTOIt, where Longi

+ 2 • Spreadingi
t

t and Shorti

+ Shorti
t

= Longi
t

(cid:0) Shorti

= d ln

PB
t

)

(cid:0)

Percentage trading positions (%)

Net trading positions

PTPOT
t

PTPNO
t

NTPAS

t

NTPDE
t

NTPLE
t

NTPOT
t

NTPNO
t

RB
t

Panel A. Full sample period

Mean
Median
Std. Dev.
Skew.
Kurt.

0.46
0.28
10.49
(cid:0) 0.37
4.48

PTPAS
t

9.76
4.85
10.49
1.33
3.01

Panel B. Period 1: Before 19 October 2021

Mean
Median
Std. Dev.
Skew.
Kurt.

1.15
1.18
10.66
(cid:0) 0.37
4.47

4.28
4.05
1.80
0.43
3.00

Panel C. Period 2: After 19 October 2021
Mean
Median
Std. Dev.
Skew.
Kurt.

(cid:0) 1.88
(cid:0) 1.69
9.60
(cid:0) 0.59
4.60

28.12
29.50
5.42
(cid:0) 2.44
10.56

PTPDE
t

2.99
2.15
2.81
0.94
2.94

1.84
1.40
1.70
0.86
3.23

6.88
7.55
2.31
(cid:0) 0.36
2.16

PTPLE
t

55.10
55.85
8.12
0.11
2.70

58.16
58.23
6.47
0.31
3.73

44.87
44.95
3.25
0.08
2.25

15.15
14.80
4.31
0.20
2.55

16.37
16.03
3.95
0.10
2.68

11.06
11.15
2.64
0.33
4.44

16.97
17.50
6.02
0.26
3.10

19.34
18.50
4.55
1.06
4.46

9.05
8.70
2.60
1.99
7.98

1199.4
112.0
2166.8
1.33
2.96

53.7
1.0
293.0
0.66
3.45

5032.4
5124.0
983.0
(cid:0) 2.65
12.68

Panel D. Tests for equality of means before and after 19 October 2021 returns and trading positions variables
t-test

(cid:0) 17.70***

(cid:0) 51.15***

14.68***

15.99***

9.35***

1.87*

(cid:0) 60.52***

Table 2
Trading positions spillover analysis in the TVP-VAR model.
This table reports spillovers of net trading positions of each trader by using the
10-day-ahead forecast error variance decomposition of the TVP-VAR model. The
ij-th entry of the upper-left 5 × 5 net positions submatrix gives the ij-th pairwise
directional spillover (i.e., the percentage of 10-day-ahead forecast error variance
of net positions i in response of shocks arising from net positions j). The right-
most (FROM) column gives total directional spillover (from) (i.e., summation of
row [from all others to i]). The bottom (TO) row gives total directional spillover
(i.e., summation of column [to all others from j]). The bottommost (NET) row
gives the difference in total directional spillover (which is calculated as TO
minus FROM). The bottom-right element is total spillover index (%).

(cid:0) 284.1
0.0
633.9
(cid:0) 1.98
6.13

(cid:0) 47.2
0.0
229.8
(cid:0) 0.89
4.19

(cid:0) 1076.6
(cid:0) 875.0
872.4
(cid:0) 0.06
1.52

(cid:0) 2492.9
(cid:0) 2048.0
2139.3
(cid:0) 0.32
1.61

(cid:0) 1643.6
(cid:0) 1046.0
1635.6
(cid:0) 0.85
2.67

(cid:0) 5334.3
(cid:0) 5454.0
651.0
0.70
3.34

495.5
129.0
1107.5
0.72
2.74

374.7
(cid:0) 21.0
1117.9
0.90
2.95

899.6
904.0
976.7
0.44
2.93

1082.1
910.0
831.7
0.96
3.27

1262.4
1087.5
796.7
0.81
2.74

479.0
372.0
645.1
3.12
15.80

14.47***

16.33***

(cid:0) 3.14***

6.66***

ΔNTPAS

t

ΔNTPDE

t

ΔNTPLE
t

ΔNTPNO

t

ΔNTPOT

t

FROM

81.85

1.34
2.42

3.01

3.41

10.19
(cid:0) 7.96

4.10

82.70
2.76

3.46

5.24

15.57
(cid:0) 1.73

3.59

5.52
57.15

17.73

23.98

50.83
7.98

3.81

2.59
17.12

70.83

2.45

25.97
(cid:0) 3.20

6.65

7.84
20.55

4.96

64.91

40.00
4.91

18.15

17.30
42.85

29.17

35.09

28.51

t

ΔNTPAS
ΔNTPDE
t
ΔNTPLE
t
ΔNTPNO
ΔNTPOT
TO
NET

t

t

6.1. Net trading positions in CME bitcoin futures

The bilateral correlation coefficients between the bitcoin futures
return and the net trading positions of the five types of traders, along
with their significance levels, are shown in Table 3. The bilateral cor-
relation analysis provides some preliminary insights into the relation-
ships between the trading activities of various traders and the bitcoin
futures returns. Table 3 shows that bitcoin futures returns are negatively
correlated with the net trading positions of dealers and leveraged funds,
but they are positively correlated with the net trading positions of asset

10

Fig. 6. Time-varying net pairwise directional spillover (NPDS) from leveraged
funds to asset managers.
Note: The dashed vertical line indicates the introduction day of BITO.

managers and non-reportable traders (retail traders). Since trading po-
sitions of asset managers reflect their crated ETFs fund flow and demand
of some retail traders, more bitcoin ETFs fund inflow would increase net-
long positions of asset managers in bitcoin futures. The net-long trading
positions of asset managers, on top of the net-long trading positions of
non-reportable traders, would then push bitcoin futures prices up. In
contrast, dealers and leveraged funds provide liquidity for the demand
of retail traders and hence generally stand on the opposite side (i.e., net-
short positions) in bitcoin futures.

Y.-L. Chen et al.

International Review of Financial Analysis 97 (2025) 103810

Table 3
Pairwise correlation analyses in the CME bitcoin futures return and net trading
positions.
This table reports the correlation coefficients among the CME bitcoin futures
return and the changes in net trading positions All of the variables are as defined
in the notes to Table 1. Correlation coefficients are reported first and their p-
values are reported in the following parentheses.

ΔNTPAS

t

ΔNTPDE

t

ΔNTPLE
t

ΔNTPOT

t

ΔNTPNO

t

RB
t

0.21
(0.00)
(cid:0) 0.21
(0.00)
(cid:0) 0.23
(0.00)
(cid:0) 0.05
(0.46)
0.25
(0.00)

ΔNTPAS

t

ΔNTPDE

t

ΔNTPLE
t

ΔNTPOT

t

(cid:0) 0.14
(0.03)
(cid:0) 0.15
(0.01)
(cid:0) 0.32
(0.00)
(cid:0) 0.15
(0.01)

0.15
(0.02)
(cid:0) 0.20
(0.00)
(cid:0) 0.17
(0.00)

(cid:0) 0.57
(0.00)
(cid:0) 0.51
(0.00)

(cid:0) 0.13
(0.05)

Given our earlier findings that the BITO introduction alters trading
activities of different types of traders, we further investigate whether
these changes in trading activities affect bitcoin futures prices and the
price spread between bitcoin futures and spot. Bessembinder (1992), De
Roon et al. (2000), Wang (2003), and Chen and Yang (2021) find that
hedging pressure is a key determinant of futures premiums and contains
explanatory power for futures returns. The rationale is that hedgers hold
the underlying asset and thus have the need to hedge by holding short
positions in the corresponding futures. The short positions for hedgers
may drive down the futures price relative to the expected value of the
spot price. Speculators who enter the market by taking long (opposite)
positions of the corresponding futures expect to be compensated for
bearing risk. Based on the hedging pressure theory, trading activities of
hedgers (speculators) may have negative (positive) impact on the price
of bitcoin futures.

In addition, stock index price movements can affect bitcoin futures
prices because changes in stock market indices often reflect broader
investor sentiment and risk appetite. During periods of heightened
optimism or pessimism in equity markets, investors may adjust their
positions in alternative assets such as bitcoin futures, influencing their
prices (Nguyen, 2022). Chan et al. (2019) find that bitcoin can hedge
and diversify against certain assets among S&P 500, Nikkei, Shanghai A-
Share, TSX, and Euro Index. Some traders may use bitcoin futures as part
of their portfolio diversification or hedging strategies. Changes in stock
index prices can prompt adjustments in these strategies, thereby
impacting demand and supply dynamics in the bitcoin futures market.
Regarding impact of market uncertainty, VIX index can influence
bitcoin futures prices in several ways. During times of heightened un-
certainty or risk aversion in traditional financial markets, investors may
seek alternative assets like bitcoin as a store of value or safe-haven asset
(Urom et al., 2020 Mariana et al., 2021). This increased demand may
drive up bitcoin futures prices. In addition, increased uncertainty in US
stock markets can lead to higher overall market volatility, affecting
trading patterns, and price dynamics in bitcoin futures markets (i.e., the
volatility spillovers in different financial assets). In the regression ana-
lyses, we include stock index price movements and market uncertainty
as control variables to statistically account for their potential influence
on bitcoin futures prices and futures basis.

Similar to De Roon et al. (2000) and Chen and Yang (2021), to
examine the impact of different trading positions on bitcoin futures, we
employ the following regression models:

RB

t+1

= β0

+ β1DBITO
)

t

+ β2ΔNTPi
+ β5RSP

+ β3
+ β6RB

ΔNTPi
t
+ et+1

t

t

t

+ β4RVIX

t

• DBITO
t

(cid:0)

and

(8)

11

BasisB

t+1

= β0

+ β1DBITO
)

t

+ β2ΔNTPi
+ β5RSP

+ β3
ΔNTPi
t
+ β6BasisB

t

t

t

+ β4RVIX

t

• DBITO
t

(cid:0)

+ et+1,

(9)

where RB, RVIX, and RSP represent the return (i.e., log-difference) of CME
bitcoin futures, VIX index, and S&P 500 index futures (times 100),
respectively. BasisB represents futures basis (i.e., futures price minus
spot price). NTPi refers to the net trading positions held by type i traders
(NTPi = Longi (cid:0) Shorti), where i = AS, DE, LE, OT, and NO, which
respectively refer to asset managers, dealers, leveraged funds, other
reportable traders, and non-reportable traders. DBITOrepresents the BITO
introduction dummy which equals to one after the introduction of BITO
and zero otherwise. Price movements of stock index and market un-
certainty may also affect the bitcoin futures price dynamics and thus are
included as control variables. Net trading positions among different
types of traders may exhibit a high correlation, so we avoid the collin-
earity issue by considering NTPi for each type i separately in Eqs. (8) and
(9).

The estimation results of Eqs. (8) and (9) are reported in Table 4. We
find that the coefficients of BITO introduction dummy are significantly
negative, but trading activities of the five types of traders have insig-
nificant impact on subsequent bitcoin futures price movements. The
estimated coefficients of interaction terms of BITO introduction and net
trading positions are also insignificant, suggesting that the BITO intro-
duction does not affect the impact of trading activities on bitcoin futures
returns.

In addition, Table 4 shows that the estimated coefficient of asset
managers trading on subsequent bitcoin futures basis is insignificantly
negative, but the estimated coefficient of the interaction term of BITO
introduction and asset managers trading is significantly positive. This
result suggests that the BITO introduction strengthens the trading role of
asset managers and their increased long positions help drive up bitcoin
futures prices, leading to a higher basis. Zhong et al. (2004), Chau et al.
(2015), Ngene et al. (2018), and Ngene and Wang (2024) highlight the
role of the basis as a signal of arbitrage opportunities between spot and
futures markets.15 These studies indicate that rational speculators and
feedback traders actively participate in both markets to exploit dis-
crepancies in the basis, thereby influencing trading behavior and prof-
itability. The introduction of BITO ETF, as a new financial instrument,
may indeed alter the dynamics of arbitrage activities among spot, ETF,
and futures markets. Specifically, BITO ETF could attract asset managers
to trade and change liquidity conditions, which may affect the arbitrage
opportunities in these markets.

Finally, the coefficients of other variables are not significant,
implying that the BITO introduction and trading positions of other
traders do not have significant impact on futures basis. These results
indicate that the trading activities in bitcoin futures may be different
from those in traditional futures, such as equity or commodity. The BITO
introduction and asset managers’ trading positions can affect bitcoin
futures prices and thus may affect market quality in bitcoin futures.

6.2. Percent trading positions and market quality in CME bitcoin futures
after the BITO introduction

Since the previous literature has documented the effect of ETFs
introduction on market quality, we analyze the impact of BITO intro-
duction on the market quality of bitcoin futures, focusing on three
different aspects: (1) Liquidity, (2) Volatility, and (3) Price efficiency.
We use various methods to measure liquidity, volatility, and price effi-
ciency to check the robustness of our results. Specifically, we consider

15 We appreciate an anonymous reviewer for suggesting those relevant studies
to help explain the relation between the basis and arbitrage opportunities in
these markets.

Y.-L. Chen et al.

International Review of Financial Analysis 97 (2025) 103810

Table 4
Price changes, futures basis, and trading positions in the CME bitcoin futures
before and after the introduction of BITO.
This table shows results from individual regressions of bitcoin futures market
price changes and futures basis on their factors and reports the estimations of the
following model:
+ β1DBITO
RB

+ β2ΔNTPi

+ β4RVIX

+ β5RSP

+ β6RB

+ et+1

= β0

• DBITO
t

ΔNTPi
t

+ β3

t+1

)

(cid:0)

t

t

t

t

t

(and)
BasisB

t+1

= β0

+ β1DBITO

t

+ β2ΔNTPi

t

+ β3

(cid:0)

ΔNTPi
t

• DBITO
t

)

+ β4RVIX

t

+ β5RSP

t

+ β6BasisB

t

+ et+1,

where RB, RVIX, and RSP represent the return of CME bitcoin futures, VIX index,
and S&P 500 index futures (time 100). BasisB represent futures basis. NTPi refer
to the net trading positions held by type i traders (NTPi = Longi (cid:0) Shorti), where
i = AS, DE, LE, OT, and NO, which respectively refer to asset managers, dealers,
leveraged funds, other-reportable traders, and non-reportable traders. Co-
efficients on control variables are estimated but not tabulated. ***, **, and *
indicate significant at the 1 %, 5 %, and 10 % levels, respectively.

(1) Asset managers

(2) Dealers

RB

BasisB

Variable

RB

Variable

Intercept

DBITO

ΔNTPAS

ΔNTPAS • DBITO

Adj.R2

1.28
(0.86)
(cid:0) 3.79***
(1.35)
(cid:0) 0.01
(0.01)
0.01
(0.01)
0.03

32.57
(25.31)
12.11
(61.38)
(cid:0) 0.06
(0.11)
0.25**
(0.10)
0.07

(3) Leveraged funds

Intercept

DBITO

ΔNTPDE

ΔNTPDE • DBITO

Adj.R2

1.28
(0.78)
(cid:0) 3.43**
(1.67)
0.01
(0.01)
(cid:0) 0.01
(0.01)
0.03

BasisB

31.97
(28.21)
24.19
(59.42)
0.15
(0.24)
(cid:0) 0.35
(0.32)
0.05

(4) Other-reportable
traders
RB
1.28
(0.78)
(cid:0) 3.69**
(1.65)
0.01
(0.01)
(cid:0) 0.01
(0.01)
0.03

BasisB
26.14
(22.93)
17.92
(48.17)
(cid:0) 0.01
(0.05)
(cid:0) 0.04
(0.09)
0.04

Variable
Intercept

DBITO

ΔNTPLE

ΔNTPLE • DBITO

Adj.R2

RB
1.26
(0.78)
(cid:0) 3.49**
(1.64)
0.01
(0.01)
0.01
(0.01)
0.03

BasisB
25.91
(22.89)
19.27
(48.03)
0.02
(0.04)
(cid:0) 0.05
(0.08)
0.04

Variable
Intercept

DBITO

ΔNTPOT

ΔNTPOT • DBITO

Adj.R2

Variable
Intercept

DBITO

ΔNTPNO

ΔNTPNO • DBITO

Adj.R2

(5) Non-reportable
traders
RB
1.24
(0.78)
(cid:0) 3.48**
(1.65)
(cid:0) 0.01
(0.01)
0.01
(0.01)
0.03

BasisB
24.91
(20.82)
19.85
(54.96)
(cid:0) 0.04
(0.05)
(cid:0) 0.03
(0.16)
0.04

t

(cid:0)

)

t(cid:0) 1

+ ej

+ β3

PTPi
t

+ β6Lj

• DBITO
t

+ β5RSP
t

+ β4RVIX

+ β2PTPi
t

+ β1DBITO
t

Table 5
Market liquidity and trading positions in the CME bitcoin futures.
This table shows results from individual regressions of bitcoin futures market
liquidity on its factors and reports the estimations of the following model: Lj
t =
β0
t, where
Lj are the market liquidity measurements of CME bitcoin futures include Ami-
hud’s illquidity (j = Amihud, times 105) and average daily volume (j = Volume,
divided by 104). DBITOrepresent the BITO introduction dummy which equals to
one after the introduction of BITO ETF and zero otherwise. PTPi, which refer to
the percentage trading positions held by type i traders, where i = AS, DE, LE, OT,
and NO, which respectively refer to (1) asset managers, (2) dealers, (3) lever-
=
aged funds, (4) other -reportable traders, and (5) non-reportable traders. PTPi
(
t
Longi
t

t refer to the
long and short positions held by type i traders on t, MTOIt is the market’s total
open interest, and Spreadingi
t measures the extent to which type i traders holds
equal long and short futures positions. Coefficients on control variables are
estimated but not tabulated. ***, **, and * indicate significant at the 1 %, 5 %,
and 10 % levels, respectively.

)
/MTOIt, where Longi

+ 2 • Spreadingi
t

t and Shorti

+ Shorti
t

Variable

Intercept

DBITO

PTPAS

PTPAS • DBITO

Adj.R2

Variable
Intercept

DBITO

PTPLE

PTPLE • DBITO

Adj.R2

Variable
Intercept

DBITO

PTPNO

PTPNO • DBITO

Adj.R2

(1) Asset managers

(2) Dealers

LAmihud

LVolume

Variable

LAmihud

LVolume

3.69***
(0.53)
(cid:0) 2.55**
(1.05)
0.17
(0.10)
(cid:0) 0.20*
(0.11)
0.04

0.74***
(0.09)
0.23**
(0.11)
(cid:0) 0.04**
(0.02)
0.03**
(0.01)
0.36

Intercept

DBITO

PTPDE

PTPDE • DBITO

Adj.R2

3.57***
(0.11)
(cid:0) 2.43**
(1.10)
(cid:0) 0.33***
(0.10)
0.18
(0.18)
0.07

0.51***
(0.05)
0.33***
(0.11)
0.03*
(0.02)
(cid:0) 0.02
(0.02)
0.35

(4) Other-reportable
traders
LAmihud
3.74***
(0.08)
(cid:0) 1.78*
(1.00)
(cid:0) 0.05
(0.04)
0.05
(0.14)
0.03

LVolume
0.55***
(0.11)
0.06
(0.20)
0.01
(0.01)
0.01
(0.01)
0.35

Variable
Intercept

DBITO

PTPOT

PTPOT • DBITO

Adj.R2

(3) Leveraged funds

LAmihud
0.49
(1.70)
(cid:0) 4.39***
(1.03)
0.04
(0.03)
(cid:0) 0.10
(0.10)
0.03

LVolume

0.27
(0.24)
0.51***
(0.16)
0.01
(0.00)
0.00
(0.01)
0.35

(5) Non-reportable
traders
LAmihud
2.53***
(0.84)
(cid:0) 1.89*
(1.02)
0.02
(0.04)
0.03
(0.14)
0.03

LVolume
0.81***
(0.13)
0.20
(0.20)
(cid:0) 0.01*
(0.00)
0.02
(0.02)
0.35

the Amihud’s illiquidity and trading volume to measure market liquidity
and adopt weekly realized volatility based on 1-min, 5-min, and 20-min
bitcoin futures returns variance. We measure price efficiency using two
standard proxies: pricing error based on Hasbrouck (1993) and variance
ratios, which have been adopted by Boehmer and Kelley (2009) and

Chen and Xu (2021).

(1) For liquidity (or illiquidity), we utilize Huang (2024) method-
ology to assess liquidity indicators for bitcoin futures across three di-
mensions: liquidity depth, resilience, and tightness.16

16 We thank an anonymous reviewer for suggesting the consideration of
different liquidity indicators such as liquidity depth, tightness, and resilience
(Huang, 2024). Due to space constraint, the estimation results of LRoll
and
LHasbrouck
are not shown here but are available upon request. The estimation
t
results from these different liquidity indicators are consistent, supporting our
finding that the BITO introduction strengthens the trading role of asset man-
agers and their increased trading positions improve market liquidity.

t

12

Y.-L. Chen et al.

International Review of Financial Analysis 97 (2025) 103810

coefficients of other traders’ percentage trading positions variables are
insignificant, except those of dealers, suggesting that dealers’ trading
improves liquidity in bitcoin futures.

(2) For volatility, we use one-minute, five-minute, and twenty-
minute futures returns during a week to calculate realized variances.
These volatility series are highly correlated, as shown in Fig. 2, so we
only report the analyses of one-minute and five-minute realized vari-
ances. We examine the impact of different trading positions on the
volatility of bitcoin futures by employing the following regression
model:

Vj
t

= β0

+ β1DBITO
)

t

+ β2PTPi

t

+ β3

(cid:0)

PTPi
t
+ β6Vj

• DBITO
t

+ β4RVIX

t

+ β5RSP

t

+ ej
t

,

(11)

t(cid:0) 1

where Vj
is the market volatility measure of CME bitcoin futures,
including one-minute realized variance (j = 1min, with logarithmic
transformation) and five-minute realized variance (j = 5min, with log-
arithmic transformation). Other factors are the same as those in Eq. (8).
The estimation results of Eq. (11) are reported in Table 6, which
shows that the coefficients of BITO introduction dummy are all insig-
nificant, and so are the coefficients of percentage trading positions of all
types of traders. Only the estimated coefficient of the interaction term of
BITO introduction and dealers’ percentage trading position is signifi-
cantly negative, indicating that dealers may help stabilize bitcoin fu-
tures after the introduction of BITO. Since dealers are large banks,
serving as market makers, the result seems reasonable. However, the
participation of dealers in bitcoin futures is still quite low, relative to
other futures markets.

(3) For price efficiency, we use the pricing error of Hasbrouck (1993)
and variance ratios during a week to measure market efficiency. We
examine the impact of different trading positions on the price efficiency
of bitcoin futures by employing the following regression model:
(cid:0)

MEj
t

= β0

+ β1DBITO
)

t

+ β2PTPi

t

+ β3

• DBITO
t

+ β4RVIX

t

+ β5RSP

t

PTPi
t
+ β6MEj

+ ej
t

,

(12)

t(cid:0) 1

where MEj are the market efficiency measurements in bitcoin futures,
including the pricing error based on Hasbrouck (1993) (j = PE and RPE)
and variance ratios (j = ∣1 (cid:0) VR(n, m)∣, times 102). PE is Hasbrouck’s
pricing error variance (σ2
pe), while RPE is the relative pricing error
)
+ σ2
m

, which measures the pricing error variance

calculated as σ2
pe

(
/

σ2
pe

as a fraction of total price variance. Smaller PE or RPE measure repre-
sents better market efficiency. We discuss Hasbrouck’s pricing error
method in detail in Appendix B. Other factors are the same as those in
Eq. (8).

A random walk implies that the ratio of long-term to short-term re-
turn variances, measured per unit of time, equals 1. We compute |1 (cid:0) VR
(n, m)| for bitcoin futures returns to measure price efficiency, where VR
(n, m) is the ratio of the bitcoin futures return variance over “m” periods
to their return variance over “n” periods, with each divided by the
respective length of the period. Smaller |1 (cid:0) VR(n, m)| represents better
market efficiency. We consider weekly measures based on |1 (cid:0) VR(1,
5)|, |1 (cid:0) VR(1,20)|, and |1 (cid:0) VR(1, 60)| to analyze the price efficiency.
The estimation results of Eq. (12) are reported in Table 7, which
shows that the coefficients of BITO introduction dummy and those of

1. Liquidity Depth: This refers to the presence of ample orders on both
sides of the current trading price, reflecting the impact of order flow
on prices. We adopt methods from Huang (2024) and Amihud (2002)
to estimate stock illiquidity, measured by the absolute (percentage)
price change relative to daily trading volume (LAmihud). Additionally,
we follow Pagano (1989) and Brennan and Subrahmanyam (1995)
by considering average daily trading volume (LVolume) as a measure of
liquidity depth.

t

√

= 2

̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅
(cid:0) COV(ΔPt, ΔPt(cid:0) 1)

2. Liquidity Resilience: Liquidity resilience assesses how quickly mar-
kets absorb new orders to correct imbalances, potentially moving
prices away from fundamental values. Following Huang (2024) and
Roll (1984), we calculate resilience through the covariance of suc-
cessive daily returns: LRoll
, where “COV” is
the first-order serial covariance of price changes in bitcoin futures.
3. Liquidity Tightness: Tightness in liquidity measures transaction
costs, such as bid-ask spread and implicit cost. Huang (2024) uses the
relative bid-ask spread as a proxy for liquidity tightness, which
measures market liquidity based on the ratio of the bid-ask spread to
the average price. Due to unavailability of intra-day bid and ask
quotes data, we use the Gibbs estimate of bid–ask spread (Hasbrouck,
2004) to proxy the bid-ask spread for the bitcoin futures (LHasbrouck
),
following Chen and Yang (2024). Hasbrouck proposes the technique
to examine the bid–ask spread based on Markov chain Monte Carlo
estimation to deal with the absence of bid and ask quotes and, pro-
vides a detailed introduction of the method of the Gibbs estimate.

t

=

⃒
⃒
RB
t

The weekly Amihud illiquidity measure is defined as follows:
⃒
⃒/Volumet, where RB and Volume represent the weekly re-
LAmihud
t
turn and trading volume in bitcoin futures, respectively. For average
trading volume, LVolume
represents the average value in daily trading
volume during week t. Following Eqs. (8) and (9), we examine the
impact of different trading positions on bitcoin futures’ market liquidity
and employ the following regression model:

t

Lj
t

= β0

+ β1DBITO
)

t

+ β2PTPi

t

+ β3

(cid:0)

PTPi
t
+ β6Lj

• DBITO
t

+ β4RVIX

t

+ β5RSP

t

+ ej
t

,

(10)

t(cid:0) 1

where Lj represents the market liquidity measure of bitcoin futures,
including Amihud’s illquidity (j = Amihud, times 105) and average
trading volume (j = Volume, divided by 104). Other factors are the same
as those in Eq. (8), except PTPi, which refers to the percentage trading
positions held by type i traders. We consider PTPi, instead of NTPi, to
examine the effect of trading activities on market liquidity because PTPi
does not depend on the trading direction of long or short. The per-
centage trading positions among different types of traders may exist a
high correlation, so we avoid the collinearity issue by considering PTPi
for each type i separately in the Eq. (10).

t

The estimation results of Eq. (10) are reported in Table 5, which
shows that the coefficients of BITO introduction dummy on Amihud’s
illiquidity measure (LAmihud
) are all significantly negative, suggesting
that the BITO introduction reduces market illiquidity in bitcoin futures.
In addition, the coefficients of BITO introduction dummy on LVolume
are
all positive, although two of them are not significant. These results
indicate that the market liquidity in the bitcoin futures improves after
the BITO introduction.

t

On the other side, the estimated coefficient of percentage trading
positions of asset managers on Amihud’s illiquidity measure is insig-
nificantly positive, but the estimated coefficient of the interaction term
of BITO introduction and their trading percentage is significantly
negative. In addition, the coefficient of the interaction term of BITO
introduction and asset managers’ percentage trading positions on
trading volume is significantly positive. These results suggest that the
BITO introduction strengthens the trading role of asset managers and
their increased trading positions improve market liquidity. Finally, the

13

Y.-L. Chen et al.

International Review of Financial Analysis 97 (2025) 103810

(cid:0)

)

PTPi
t

+ β3

• DBITO
t

+ β2PTPi
t

Table 6
Market volatility and trading positions in the CME bitcoin futures.
This table shows results from individual regressions of bitcoin futures market volatility on its factors and reports the estimations of the following model: Vj
β1DBITO
t, where Vj are the market volatility measurements of CME bitcoin futures include one-minute
t
realized variance (j = 1min, with logarithmic transformation) and five-minute realized variance(j = 5min, with logarithmic transformation). DBITOrepresent the
BITO introduction dummy which equals to one after the introduction of BITO ETF and zero otherwise. PTPi, which refer to the percentage trading positions held by
type i traders, where i = AS, DE, LE, OT, and NO, which respectively refer to (1) asset managers, (2) dealers, (3) leveraged funds, (4) other-reportable traders, and (5)
non-reportable traders. PTPi
t
is the market’s total open interest, and Spreadingi
variables are estimated but not tabulated. ***, **, and * indicate significant at the 1 %, 5 %, and 10 % levels, respectively.

t measures the extent to which type i traders holds equal long and short futures positions. Coefficients on control

t refer to the long and short positions held by type i traders on t, MTOIt

)
/MTOIt, where Longi

+ 2 • Spreadingi
t

(
Longi
t

t and Shorti

+ β4RVIX

+ Shorti
t

+ β5RSP
t

+ β6Vj

t = β0

+ ej

t(cid:0) 1

=

+

t

Variable

Intercept

DBITO

PTPDE

PTPDE • DBITO

Adj.R2

Variable
Intercept

DBITO

PTPOT

PTPOT • DBITO

Adj.R2

(2) Dealers

V1min

(cid:0) 15.32***
(0.91)
0.45
(0.31)
0.05
(0.05)
(cid:0) 0.12**
(0.05)

0.44

(4) Other-reportable traders
V1min
(cid:0) 15.20***
(0.77)
(cid:0) 1.28**
(0.60)
(cid:0) 0.02
(0.01)
0.08**
(0.04)
0.45

V5min

(cid:0) 13.57***
(0.94)
0.51
(0.31)
0.06
(0.05)
(cid:0) 0.14**
(0.05)

0.38

V5min
(cid:0) 13.41***
(0.80)
1.32**
(0.64)
(cid:0) 0.02
(0.01)
0.08**
(0.04)
0.38

Variable

Intercept

DBITO

PTPAS

PTPAS • DBITO

Adj.R2

Variable
Intercept

DBITO

PTPLE

PTPLE • DBITO

Adj.R2

Variable
Intercept

DBITO

PTPNO

PTPNO • DBITO

Adj.R2

(1) Asset managers

V1min

(cid:0) 13.55***
(0.80)
0.01
(0.72)
(cid:0) 0.03
(0.04)
0.02
(0.05)

0.44

(3) Leveraged funds
V1min
(cid:0) 16.15***
(1.28)
1.21
(0.94)
0.01
(0.01)
(cid:0) 0.02
(0.01)
0.44

(5) Non-reportable traders
V1min
(cid:0) 15.40***
(0.86)
(cid:0) 0.53
(0.66)
0.01
(0.02)
0.03
(0.05)
0.43

V5min

(cid:0) 13.55***
(0.80)
0.01
(0.72)
(cid:0) 0.03
(0.04)
0.02
(0.05)

0.37

V5min
(cid:0) 14.25***
(1.12)
1.07
(1.71)
0.01
(0.01)
(cid:0) 0.02
(0.03)
0.38

V5min
(cid:0) 13.80***
(0.91)
(cid:0) 0.40
(0.69)
0.01
(0.02)
0.02
(0.05)
0.38

percentage trading positions are mostly insignificant. Only the esti-
mated coefficient of the interaction term of BITO introduction and
dealers’ percentage trading position is significantly negative, suggesting
that dealers may reduce the pricing errors of bitcoin futures after the
BITO introduction. To the extent that low pricing errors may reduce
transitory volatility, this result is in line with the earlier finding that
dealers may help reduce the volatility of bitcoin futures. In sum, we do
not find any evidence that the BITO introduction affects the efficiency
and volatility in bitcoin futures, but dealers’ trading after the BITO
introduction may reduce market volatility and enhance market
efficiency.17

17 We thank an anonymous reviewer for highlighting the excess kurtosis of the
data and suggesting the consideration of quantile regression analyses. Due to
space constraints, the estimation results of the quantile regression analyses are
not shown here but are available upon request. The results from these analyses
consistently support that the introduction of BITO strengthens the trading role
of asset managers and their increased trading positions improve market
liquidity. Additionally, the introduction of BITO does not affect the efficiency
and volatility of bitcoin futures.

14

7. Market quality in CME bitcoin futures around the BITO
introduction

To better understand the impact of BITO introduction, we further
analyze the liquidity, volatility, and price efficiency in bitcoin futures at
a daily frequency around the BITO introduction day. This analysis can
provide additional insights because about $1.2 billion flowed into BITO
during its first three days on the market. Since the TFF report does not
provide daily or higher frequency data on traders’ positions, our ana-
lyses in Section 5 may be more relevant to the impact of medium- to
long-term trading on market quality in bitcoin futures. Now, we focus on
short-term liquidity, volatility, informed trading, and price efficiency in
bitcoin futures immediately before and after the BITO introduction
without considering trader positions.

Analyzing liquidity, volatility, and price efficiency in bitcoin futures
around the BITO introduction day can provide a rather clean result that
can be attributed mainly to the BITO introduction and less to other
market disturbances. In addition, we use order imbalance and absolute
value in order imbalance to measure informed trading and asymmetric
information (Chordia et al., 2002 Bernile et al., 2016). We plot the
liquidity, volatility, and price efficiency measures in bitcoin futures on a
daily basis surrounding the BITO introduction day in Fig. 7. We find that

Y.-L. Chen et al.

International Review of Financial Analysis 97 (2025) 103810

Table 7
Market efficiency and trading positions in the CME bitcoin futures.
This table shows results from individual regressions of bitcoin futures market efficiency on its factors and reports the estimations of the following model: MEj
β1DBITO
t
based on Hasbrouck (1993) (j = PE and RPE) and variance ratios (j = |1 (cid:0) VR[n, m] |, times 102). PE measurement is Hasbrouck’s pricing error variance (σ2

+
t, where MEj are the market efficiency measurements of CME bitcoin futures include pricing error
pe) and RPE is

+ β2PTPi
t

+ β6MEj

+ β4RVIX

+ β5RSP
t

• DBITO
t

t = β0

PTPi
t

+ β3

+ ej

t(cid:0) 1

)

(cid:0)

t

the relative pricing error is calculated as σ2
pe

σ2
pe

+ σ2
m

, which is the relative mispricing measurement, examined by the pricing error variance as a fraction of total

price variance. DBITOrepresent the BITO introduction dummy which equals to one after the introduction of BITO ETF and zero otherwise. PTPi, which refer to the
percentage trading positions held by type i traders, where i = AS, DE, LE, OT, and NO, which respectively refer to (1) asset managers, (2) dealers, (3) leveraged funds,
+ Shorti
(4) other-reportable traders, and (5) non-reportable traders. PTPi
t
t
positions held by type i traders on t, MTOIt is the market’s total open interest, and Spreadingi
t measures the extent to which type i traders holds equal long and short
futures positions. Coefficients on control variables are estimated but not tabulated. ***, **, and * indicate significant at the 1 %, 5 %, and 10 % levels, respectively.

)
/MTOIt, where Longi

t refer to the long and short

+ 2 • Spreadingi
t

t and Shorti

(
Longi
t

=

(
/

)

Variable

Pricing errors

MEPE

(1) Percentage trading positions of asset managers
Intercept

(2) Percentage trading positions of dealers
Intercept

(3) Percentage trading positions of leveraged funds
Intercept

(4) Percentage trading positions of other reportable traders
Intercept

(5) Percentage trading positions of non-reportable traders
Intercept

DBITO

PTPAS

PTPAS • DBITO

Adj.R2

DBITO

PTPDE

PTPDE • DBITO

Adj.R2

DBITO

PTPLE

PTPLE • DBITO

Adj.R2

DBITO

PTPOT

PTPOT • DBITO

Adj.R2

DBITO

PTPNO

PTPNO • DBITO

Adj.R2

(cid:0) 17.46***
(0.29)
(cid:0) 1.99
(9.01)
0.15
(0.50)
(cid:0) 0.19
(0.58)
0.08

(cid:0) 17.58***
(0.17)
(cid:0) 0.19
(0.67)
0.11*
(0.06)
(cid:0) 0.18*
(0.11)
0.08

(cid:0) 18.01***
(1.03)
(cid:0) 1.11
(2.80)
(cid:0) 0.01
(0.01)
(cid:0) 0.03
(0.06)
0.08

(cid:0) 16.31***
(0.46)
(cid:0) 3.06***
(0.92)
(cid:0) 0.06**
(0.02)
0.19
(0.17)
0.11

(cid:0) 17.57***
(0.51)
(cid:0) 0.88
(0.88)
(cid:0) 0.01
(0.02)
0.05
(0.07)
0.08

MERPE

(cid:0) 3.73***
(0.21)
(cid:0) 0.31
(0.52)
0.02
(0.04)
(cid:0) 0.04
(0.05)
0.06

(cid:0) 3.63***
(0.14)
(cid:0) 0.42
(0.56)
0.01
(0.05)
(cid:0) 0.01
(0.09)
0.06

(cid:0) 2.90**
(1.11)
(cid:0) 0.55
(2.36)
(cid:0) 0.01
(0.01)
(cid:0) 0.02
(0.02)
0.07

(cid:0) 2.06***
(0.78)
(cid:0) 1.53*
(0.81)
(cid:0) 0.03
(0.02)
0.08
(0.06)
0.08

(cid:0) 2.21**
(0.97)
(cid:0) 0.59
(0.72)
(cid:0) 0.01
(0.02)
0.02
(0.06)
0.08

Variance ratios

|1(cid:0) VR(1,5|)

ME

|1(cid:0) VR(1,20) |

ME

|1(cid:0) VR(1,60) |

ME

12.31***
(2.61)
(cid:0) 0.07
(9.79)
0.80
(0.55)
(cid:0) 0.77
(0.64)
0.04

16.21***
(1.52)
(cid:0) 0.33
(5.99)
(cid:0) 0.25
(0.60)
(cid:0) 0.19
(0.99)
0.04

22.54**
(8.98)
(cid:0) 28.63
(25.50)
(cid:0) 0.11
(0.15)
0.53
(0.55)
0.04

19.59***
(4.30)
(cid:0) 1.63
(8.63)
(cid:0) 0.23
(0.25)
0.23
(0.70)
0.04

9.11**
(4.35)
3.41
(7.73)
0.34
(0.22)
(cid:0) 0.31
(0.70)
0.05

20.62***
(2.93)
(cid:0) 1.85
(11.09)
0.16
(0.62)
(cid:0) 0.05
(0.72)
0.03

20.39***
(1.72)
(cid:0) 4.14
(6.77)
(cid:0) 0.25
(0.68)
0.29
(1.13)
0.03

10.95
(10.21)
(cid:0) 11.41
(29.19)
(cid:0) 0.15
(0.17)
0.22
(0.63)
0.04

26.69***
(4.86)
(cid:0) 7.57
(9.84)
(cid:0) 0.41
(0.28)
0.17
(0.80)
0.04

18.82***
(5.02)
6.94
(8.91)
0.05
(0.25)
0.45
(0.81)
0.03

7.47***
(1.92)
(cid:0) 0.99
(7.31)
0.58
(0.48)
(cid:0) 0.57
(0.49)
0.04

11.22***
(1.09)
(cid:0) 4.63
(4.35)
(cid:0) 0.65
(0.43)
0.71
(0.72)
0.04

13.44**
(6.65)
(cid:0) 5.71
(19.36)
(cid:0) 0.05
(0.11)
0.04
(0.42)
0.03

13.03***
(3.18)
(cid:0) 5.67
(6.51)
(cid:0) 0.18
(0.18)
0.14
(0.53)
0.03

4.70
(3.19)
2.88
(5.72)
0.27*
(0.16)
(cid:0) 0.34
(0.52)
0.04

15

Y.-L. Chen et al.

International Review of Financial Analysis 97 (2025) 103810

Fig. 7. Short-term liquidity, volatility, informed trading, and price efficiency in bitcoin futures around BITO introduction.
Note: Means refer to the average values of the variables in five days before and after BITO introduction. The dashed vertical line indicates the introduction day of
BITO (10/19/2021).

Amihud’s illiquidity falls from 0.44 to 0.37, while trading volume rises
from 7782.6 to 10,711.4 from the pre-introduction to the post-
introduction days. These results suggest that the BITO introduction
improves short-term liquidity in the bitcoin futures market.

In addition, we find that the two daily price efficiency measures, PE
and RPE, jump on the BITO introduction day and then revert back to the
previous level on the fourth day of the BITO introduction. However,
informed trading and the level of asymmetric information do not seem to
change after the BITO introduction.

8. Conclusions

In this study, we investigate the introduction effect of bitcoin futures-
based ETF (BITO) on investor structure and market quality in bitcoin
futures. We adopt the TFF report to categorize major traders into
dealers, asset managers, leveraged fund managers, and other reportable
traders in bitcoin futures. Our results indicate that the BITO introduction
significantly changes the investor structure in bitcoin futures and ETF
asset managers become the major long-side participants against the

short-side hedge funds. Further, market participants in bitcoin futures
become more concentrated. However, these changes in investor struc-
ture does not impair futures market quality as the market liquidity of
bitcoin futures improves after the BITO introduction while efficiency
and volatility do not seem to be affected significantly. In contrast, for
short-term shock from the BITO introduction, we find that fund inflow of
BITO improves the liquidity in bitcoin futures during the first five days
of BITO introduction but hurts futures’ price efficiency on the first three
days of BITO introduction before reverting back to the previous level.

Our findings provide several policy implications that could be
considered by policymakers. First, we recommend supporting the crea-
tion of bitcoin futures-based ETFs because our research shows that they
do not destabilize or negatively impact the corresponding bitcoin futures
prices. Instead, they enhance market liquidity over the medium to long
term. This finding may be further validated by the introduction of the
second and third bitcoin futures ETFs, the Valkyrie Bitcoin Strategy ETF
(BTF) and the VanEck Bitcoin Strategy ETF (XBTF). Second, our study
highlights the unique market concentration in bitcoin futures, which
significantly differs from the investor structure in other futures markets.

16

Y.-L. Chen et al.

International Review of Financial Analysis 97 (2025) 103810

Large banks, or dealers, have relatively low participation in bitcoin fu-
tures, yet their involvement is crucial as they play a positive role in
reducing volatility and enhancing market efficiency. Therefore, policy-
makers may consider strategies to encourage greater dealer participa-
tion in bitcoin futures to further improve futures market quality.

We anticipate that the introduction of bitcoin spot ETFs on January
11, 2024 will influence trading in bitcoin spot, bitcoin futures, and
BITO. Due to the short sample period and thus limited data for con-
ducting empirical analyses in this stage, we do not consider the impact of
bitcoin spot ETFs. We recommend that future studies expand our
empirical analyses to investigate the impact of bitcoin spot ETFs on

market quality in bitcoin futures.

Data availability

The authors do not have permission to share data.

Acknowledgments

Yu-Lun Chen acknowledges financial support from the Ministry of
Science and Technology, Taiwan (R.O.C.) (MOST 111–2410-H-033-038-
MY3).

Appendix A

CME bitcoin futures- contract specifications.

1. CONTRACT UNIT

2. PRICE QUOTATION
3. SETTLEMENT METHOD
4. TERMINATION OF
TRADING
5. TRADING HOURS
6. LISTED CONTRACTS

5 bitcoin, as defined by the CME CF Bitcoin Reference Rate (BRR) BRR is a once a day benchmark index price for bitcoin that aggregates trade data
from multiple bitcoin-USD markets operated by major cryptocurrency exchanges.
U.S. dollars and cents per bitcoin
Cash Settled
Trading terminates at 4:00 p.m. London time on the last Friday of the contract month that is either a London or U.S. business day. If the last Friday of
the contract month is not a business day in both London and the U.S., trading terminates on the prior London or U.S. business day.
CME Globex: Sunday - Friday 5:00 p.m. - 4:00 p.m./CT with a 60-min break each day beginning at 4:00 p.m. CT
Monthly contracts listed for 6 consecutive months, quarterly contracts (Mar, Jun, Sep, Dec) listed for 4 additional quarters and a second Dec contract if
only one is listed

Source: https://www.cmegroup.com/

Appendix B

We illustrate Hasbrouck (1993) pricing error method here. According to studies of Hasbrouck (1993) and Chen and Xu (2021), asset transaction
price can be decomposed into a random-walk component and a stationary component. The random-walk component is identified with the efficient
price and the stationary component represents the difference between efficient price and the transaction price (i.e. pricing error). Hasbrouck proposes
that pricing error (i.e., the deviation of observed transaction prices from unobserved efficient prices) offers an alternative measure of the implicit
transaction costs incurred by traders and the variance of the pricing error determines how closely actual transaction prices track the efficient price.
To measure the variance of the pricing error in Hasbrouck (1993), we estimate the following vector autoregression (VAR) of bitcoin futures price

changes and trades first as follows:
rt = a0 + a1rt(cid:0) 1 + a2rt(cid:0) 2 + ⋯ + b1xt(cid:0) 1 + b2xt(cid:0) 2 + ⋯ + v1,t
xt = c0 + c1rt(cid:0) 1 + c2rt(cid:0) 2 + ⋯ + d1xt(cid:0) 1 + d2xt(cid:0) 2 + ⋯ + v2,t

,

(B1)

where rt and xt are the log-price changes and trades (according to the tick rule, we classify a buy order as 1 and a sell order as 1). v1,t and v2,t are the
zero mean and serially uncorrelated disturbances. The VAR in Eq. (B1) can be transformed to the vector moving average (VMA) in Eq. (B2) as follows:

rt = a*
xt = c*

0v1,t + a*
0v1,t + c*

1v1,t(cid:0) 1 + a*
1v1,t(cid:0) 1 + c*

2v1,t(cid:0) 2 + ⋯ + b*
2v1,t(cid:0) 2 + ⋯ + d*

0v2,t + b*
0v2,t + d*

1v2,t(cid:0) 1 + b*
1v2,t(cid:0) 1 + d*

2v2,t(cid:0) 2⋯
2v2,t(cid:0) 2⋯

,

(B2)

where the VMA coefficients can be calculated by forecasting the VAR system in Eq. (B1) by using impulse responses analysis. To calculate pricing error
(st), only the (rt = a*
2v2,t(cid:0) 2⋯) is needed, because Hasbrouck (1993) argues that an expanded
representation for pricing errors is

2v1,t(cid:0) 2 + ⋯ + b*

1v1,t(cid:0) 1 + a*

1v2,t(cid:0) 1 + b*

0v1,t + a*

0v2,t + b*

(cid:0)

)
α0v1,t + α1v1,t(cid:0) 1 + ⋯

+

(cid:0)

)
β0v2,t + β1v2,t(cid:0) 1 + ⋯

st =

+ (φt

+ γ1φt(cid:0) 1⋯),

(cid:0)

)

(cid:0)

α0v1,t + α1v1,t(cid:0) 1 + ⋯

captures pricing errors
where
due to the current and lagged trades adjustment. In addition, φt is a zero-mean, covariance-stationary process, orthogonal to all components of v1,t and
v2,t.

captures pricing errors due to the current and lagged price adjustment and

β0v2,t + β1v2,t(cid:0) 1 + ⋯

By a generalization of Beveridge and Nelson’s (BN, 1981) demonstration, αj and βj in Eq. (B3) may be computed with the BN identification re-

striction (φt
∑∞

αj = (cid:0)

k=j+1

= γ1

= ⋯ = 0) and the VMA coefficients (a*

0…), (b*

0…) in Eq. (B2):

a*
k

and βj

= (cid:0)

∑∞

k=j+1

.

b*
k

(B4)

When the coefficients appear in Eq. (B4) and we drop the φt terms, the result is an identification-invariant, best-linear estimate of st, conditional on

current and lagged vt. The pricing error variance (σ2

pe) may then be computed as

17

(B3)

)

Y.-L. Chen et al.

σ2
pe

=

∑∞

j=0

[
αj βj

]
Cov(v)

]

[

αj
βj

International Review of Financial Analysis 97 (2025) 103810

(B5)

Initially, by using tick-by-tick price and trade of bitcoin futures, we examine the pricing error variance (σ2

degree of bitcoin futures market efficiency (i.e., PE measure). To assure meaningful comparisons, we also standardize σ2
component variance and pricing error variance, [σ2
m
price efficiency for bitcoin futures market.

pe) which serves as the proxies for the
pe by the sum of random walk
pe]. A lower (standardized) relative pricing error variance (i.e., RPE measure) implies better

+σ2

References

Ackert, L. F., & Tian, Y. S. (1998). The introduction of Toronto index participation units
and arbitrage opportunities in the Toronto 35 index option market. Journal of
Derivatives, 5(4), 44–53.

Ackert, L. F., & Tian, Y. S. (2001). Efficiency in index options markets and trading in

stock baskets. Journal of Banking and Finance, 25(9), 1607–1634.

Amihud, Y. (2002). Illiquidity and stock returns: Cross-section and time-series effects.

Journal of Financial Markets, 5(1), 31–56.

Andersen, T. G., Bollerslev, T., Diebold, F. X., & Ebens, H. (2001). The distribution of
realized stock return volatility. Journal of Financial Economics, 61(1), 43–76.
Andersen, T. G., Bollerslev, T., Diebold, F. X., & Labys, P. (2003). Modeling and

forecasting realized volatility. Econometrica, 71(2), 579–625.

Antonakakis, N., Chatziantoniou, I., & Gabauer, D. (2020). Refined measures of dynamic
connectedness based on time-varying parameter vector autoregressions. Journal of
Risk and Financial Management, 13(4), 1–23.

Augustin, P., Rubtsov, A., & Shin, D. (2023). The impact of derivatives on spot markets:
Evidence from the introduction of bitcoin futures contracts. Management Science, 69
(11), 6752–6776.

Baur, D. G., & Smales, L. A. (2022). Trading behavior in bitcoin futures: Following the

“smart money”. Journal of Futures Markets, 42(7), 1304–1323.

Ben-David, I., Franzoni, F., & Moussawi, R. (2018). Do ETFs increase volatility? Journal

of Finance, 73(6), 2471–2535.

Bernile, G., Hu, J., & Tang, Y. (2016). Can information be locked up? Informed trading
ahead of macro-news announcements. Journal of Financial Economics, 121(3),
496–520.

Bessembinder, H. (1992). Systematic risk, hedging pressure, and risk premiums in futures

markets. Review of Financial Studies, 5(4), 637–667.

Boehmer, E., & Kelley, E. K. (2009). Institutional investors and the informational

efficiency of prices. Review of Financial Studies, 22(9), 3563–3594.

Box, T., Davis, R., Evans, R., & Lynch, A. (2021). Intraday arbitrage between ETFs and
their underlying portfolios. Journal of Financial Economics, 141(3), 1078–1095.
Brennan, M. J., & Subrahmanyam, A. (1995). Investment analysis and price formation in

securities markets. Journal of Financial Economics, 38(3), 361–381.

Chan, W. H., Le, M., & Wu, Y. W. (2019). Holding bitcoin longer: The dynamic hedging
abilities of bitcoin. The Quarterly Review of Economics and Finance, 71, 107–113.
Chau, F., Kuo, J. M., & Shi, Y. (2015). Arbitrage opportunities and feedback trading in
emissions and energy markets. Journal of International Financial Markets, Institutions
and Money, 36, 130–147.

Chen, Y. L., & Xu, K. (2021). The impact of RMB’s SDR inclusion on price discovery in
onshore-offshore markets. Journal of Banking and Finance, 127, Article 106124.
Chen, Y. L., & Yang, J. J. (2021). Trader positions in VIX futures. Journal of Empirical

Finance, 61, 1–17.

Chen, Y. L., & Yang, J. J. (2024). Time-varying price discovery in regular and

microbitcoin futures. Journal of Futures Markets, 44(1), 103–121.

Chordia, T., Roll, R., & Subrahmanyam, A. (2002). Order imbalance, liquidity, and

market returns. Journal of Financial Economics, 65(1), 111–130.

Chu, Q. C., & Hsieh, W. L. G. (2002). Pricing efficiency of the S&P 500 index market:

Evidence from the Standard & Poor’s depositary receipts. Journal of Futures Markets,
22(9), 877–900.

Cong, L. W., Li, X., Tang, K., & Yang, Y. (2023). Crypto wash trading. Management

Science, 69(11), 6427–6454.

Da, Z., Tang, K., Tao, Y., & Yang, L. (2023). Financialization and commodity markets

serial dependence. Management Science, 1–22.

De Roon, F. A., Nijman, T. E., & Veld, C. (2000). Hedging pressure effects in futures

markets. Journal of Finance, 55(3), 1437–1456.

Diebold, F. X., & Yilmaz, K. (2012). Better to give than to receive: Predictive directional
measurement of volatility spillovers. International Journal of Forecasting, 28(1),
57–66.

Diebold, F. X., & Yilmaz, K. (2014). On the network topology of variance decompositions:
Measuring the connectedness of financial firms. Journal of Econometrics, 182(1),
119–134.

Glosten, L., Nallareddy, S., & Zou, Y. (2021). ETF activity and informational efficiency of

underlying securities. Management Science, 67(1), 22–47.

Hajric, V. (2021). Bloomberg news. https://www.bloomberg.com/news/articles/2021-1

0-19/proshares-bitcoin-futures-etf-starts-trading-in-watershed-moment.

Hasbrouck, J. (1993). Assessing the quality of a security market: A new approach to

transaction-cost measurement. Review of Financial Studies, 6(1), 191–212.
Hasbrouck, J. (2004). Liquidity in the futures pits: Inferring market dynamics from
incomplete data. Journal of Financial and Quantitative Analysis, 39(2), 305–326.

Hegde, S. P., & McDermott, J. B. (2004). The market liquidity of DIAMONDS, Q’s, and

their underlying stocks. Journal of Banking and Finance, 28(5), 1043–1067.

Huang, S. S. (2024). Liquidity dynamics between virtual and equity markets. Journal of

International Financial Markets Institutions and Money, 91, Article 101917.

Hung, J. C., Liu, H. C., & Yang, J. J. (2021). Trading activity and price discovery in

bitcoin futures markets. Journal of Empirical Finance, 62, 107–120.

Israeli, D., Lee, C., & Sridharan, S. A. (2017). Is there a dark side to exchange traded

funds? An information perspective. Review of Accounting Studies, 22(3), 1048–1083.

Ji, Q., Li, J., & Sun, X. (2019). Measuring the interdependence between investor

sentiment and crude oil returns: New evidence from the CFTC’s disaggregated
reports. Finance Research Letters, 30, 420–425.

Kapar, B., & Olmo, J. (2019). An analysis of price discovery between bitcoin futures and

spot markets. Economics Letters, 174, 62–64.

Kurov, A. A., & Lasser, D. J. (2002). The effect of the introduction of cubes on the

Nasdaq-100 index spot-futures pricing relationship. Journal of Futures Markets, 22(3),
197–218.

Makarov, I., & Schoar, A. (2020). Trading and arbitrage in cryptocurrency markets.

Journal of Financial Economics, 135(2), 293–319.

Mariana, C. D., Ekaputra, I. A., & Husodo, Z. A. (2021). Are bitcoin and Ethereum safe-
havens for stocks during the COVID-19 pandemic? Finance Research Letters, 38,
Article 101798.

Ngene, G. M., Benefield, P., & Lynch, A. K. (2018). Asymmetric and nonlinear dynamics

in sovereign credit risk markets. Journal of Futures Markets, 38(5), 563–585.
Ngene, G. M., & Wang, J. (2024). Arbitrage opportunities and feedback trading in
regulated bitcoin futures market: An intraday analysis. International Review of
Economics and Finance, 89, 743–761.

Nguyen, K. Q. (2022). The correlation between the stock market and bitcoin during
COVID-19 and other uncertainty periods. Finance Research Letters, 46, Article
102284.

O’Hara, M. (2003). Presidential address: Liquidity and price discovery. Journal of

Finance, 58, 1335–1354.

O’Hara, M. (2020). ETFs and systemic risks. CFA Institute Research Foundation briefs. ISBN

978–1–944960-91-9. Available at SSRN.

O’Hara, M., & Ye, M. (2011). Is market fragmentation harming market quality? Journal of

Financial Economics, 100(3), 459–474.

Pagano, M. (1989). Trading volume and asset liquidity. The Quarterly Journal of

Economics, 104(2), 255–274.

Park, T. H., & Switzer, L. N. (1995). Index participation units and the performance of
index futures markets: Evidence from the Toronto 35 index participation units
market. Journal of Futures Markets, 15(2), 187–200.

Roll, R. (1984). A simple implicit measure of the effective bid-ask spread in an efficient

market. Journal of Finance, 39(4), 1127–1139.

Switzer, L. N., Varson, P. L., & Zghidi, S. (2000). Standard and Poor’s depository receipts
and the performance of the S&P 500 index futures market. Journal of Futures Markets,
20(8), 705–716.

Tiniç, M., S¸ ensoy, A., Akyildirim, E., & Corbet, S. (2022). Adverse selection in

cryptocurrency markets (SSRN working paper).

Todorov, K. (2021a). The anatomy of bond ETF arbitrage. BIS Quarterly Review (pp.

41–53).

Todorov, K. (2021b). Launch of the first US bitcoin ETF: Mechanics, impact, and risks. BIS

Quarterly Review December.

Urom, C., Abid, I., Guesmi, K., & Chevallier, J. (2020). Quantile spillovers and
dependence between bitcoin, equities and strategic commodities. Economic
Modelling, 93, 230–258.

Wang, C. (2003). The behavior and performance of major types of futures traders.

Journal of Futures Markets, 23(1), 1–31.

Wu, J., Xu, K., Zheng, X., & Chen, J. (2021). Fractional cointegration in bitcoin spot and

futures markets. Journal of Futures Markets, 41(9), 1478–1494.

Zhang, S., Zhang, D., Zheng, J., Aerts, W., & Xu, D. (2023). Plus token and investor

searching behavior: A cryptocurrency Ponzi scheme. Accounting and Finance, 63(4),
4713–4728.

Zhang, Y. (2015). The securitization of gold and its potential impact on gold stocks.

Journal of Banking and Finance, 58, 309–326.

Zhong, M., Darrat, A. F., & Otero, R. (2004). Price discovery and volatility spillovers in
index futures markets: Some evidence from Mexico. Journal of Banking and Finance,
28(12), 3037–3054.

Zhu, P., Zhang, X., Wu, Y., Zheng, H., & Zhang, Y. (2021). Investor attention and
cryptocurrency: Evidence from the bitcoin market. PLoS ONE, 16(2), 1–28.

18

