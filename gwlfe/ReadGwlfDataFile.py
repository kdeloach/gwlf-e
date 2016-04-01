# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import numpy as np

from .enums import YesOrNo
from . import PrelimQualCalculations


def ReadAllData(z):
    z.AvCN = 0
    z.AvKF = 0
    z.UrbAreaTotal = 0
    z.RurAreaTotal = 0
    z.PcntUrbanArea = 0
    z.AreaTotal = 0
    z.AvCNUrb = 0
    z.AvCNRur = 0

    z.NLU = z.NRur + z.NUrb

    z.NYrs = z.WxYrs
    z.DimYrs = z.WxYrs

    # DECLARE ALL VARIABLES
    z.AnimalFlag = 0
    z.AvGRStreamFC = 0
    z.AvGRStreamN = 0
    z.AvGRStreamP = 0

    # Redimension all of the varables used in the model run
    z.Month = np.zeros(12)
    z.Landuse = np.zeros(16)
    z.Imper = np.zeros(16)
    z.CNI = np.zeros((3, 16))
    z.CNP = np.zeros((3, 16))
    z.LoadRateImp = np.zeros((16, 3))
    z.LoadRatePerv = np.zeros((16, 3))
    z.DisFract = np.zeros((16, 3))
    z.UrbBMPRed = np.zeros((16, 3))
    z.TotSusSolids = np.zeros((16,))
    z.Contaminant = np.zeros(3)
    z.DayHrs = np.zeros(12)
    z.Grow = np.zeros(12)
    z.KV = np.zeros(12)
    z.d = np.zeros(12)
    z.KVD = np.zeros(12)
    z.CV = np.zeros(12)
    z.Acoef = np.zeros(12)
    z.Area = np.zeros(16)
    z.AreaE = np.zeros(16)
    z.KLSCP = np.zeros(16)
    z.CN = np.zeros(16)
    z.KF = np.zeros(16)
    z.LS = np.zeros(16)
    z.C = np.zeros(16)
    z.P = np.zeros(16)
    z.NewCN = np.zeros((12, 16))
    z.AntMoist = np.zeros(5)
    z.PcntET = np.zeros(12)
    z.StreetSweepNo = np.zeros(12)
    z.ISRR = np.zeros(6)
    z.ISRA = np.zeros(6)
    z.NitrConc = np.zeros(16)
    z.PhosConc = np.zeros(16)
    z.ManNitr = np.zeros(16)
    z.ManPhos = np.zeros(16)
    z.UrbanNitr = np.zeros(16)
    z.UrbanPhos = np.zeros(16)
    z.PointNitr = np.zeros(12)
    z.PointPhos = np.zeros(12)
    z.PointFlow = np.zeros(12)
    z.AvStreamFlow = np.zeros(12)
    z.AvPrecipitation = np.zeros(12)
    z.AvEvapoTrans = np.zeros(12)
    z.AvGroundWater = np.zeros(12)
    z.AvRunoff = np.zeros(12)
    z.AvErosion = np.zeros(12)
    z.AvSedYield = np.zeros(12)
    z.AFON = np.zeros(12)
    z.AFOP = np.zeros(12)
    z.AvLoad = np.zeros((12, 3))
    z.AvLuLoad = np.zeros((16, 3))
    z.UrbSedLoad = np.zeros((16, 12))
    z.Load = np.zeros((z.DimYrs, 12, 3))
    z.DisLoad = np.zeros((z.DimYrs, 12, 3))
    z.AvGroundNitr = np.zeros(12)
    z.AvGroundPhos = np.zeros(12)
    z.AvDisNitr = np.zeros(12)
    z.AvTotNitr = np.zeros(12)
    z.AvDisPhos = np.zeros(12)
    z.AvTotPhos = np.zeros(12)
    z.AvLuRunoff = np.zeros(16)
    z.AvLuErosion = np.zeros(16)
    z.AvLuSedYield = np.zeros(16)
    z.AvLuDisNitr = np.zeros(16)
    z.AvLuTotNitr = np.zeros(16)
    z.AvLuDisPhos = np.zeros(16)
    z.AvLuTotPhos = np.zeros(16)
    z.UplandN = np.zeros((z.DimYrs, 12))
    z.UplandP = np.zeros((z.DimYrs, 12))
    z.BSed = np.zeros(16)
    z.UrbanSed = np.zeros(16)
    z.UrbanErosion = np.zeros(16)
    z.ErosWashoff = np.zeros((16, 12))
    z.QRunoff = np.zeros((16, 12))
    z.AgQRunoff = np.zeros((16, 12))
    z.RurQRunoff = np.zeros((16, 12))
    z.UrbQRunoff = np.zeros((16, 12))
    z.UrbRunoffCm = np.zeros((z.DimYrs, 12))
    z.UrbRunoffLiter = np.zeros((z.DimYrs, 12))
    z.DailyFlow = np.zeros((z.DimYrs, 12, 31))
    z.DailyFlowMGD = np.zeros((z.DimYrs, 12, 31))
    z.DailyFlowGPM = np.zeros((z.DimYrs, 12, 31))
    z.DailyPtSrcFlow = np.zeros((z.DimYrs, 12, 31))
    z.NumPondSys = np.zeros(12)
    z.NumNormalSys = np.zeros(12)
    z.NumShortSys = np.zeros(12)
    z.NumDischargeSys = np.zeros(12)
    z.NumSewerSys = np.zeros(12)
    z.DailyLoad = np.zeros((50, 12, 31))
    z.SepticsDay = np.zeros(12)
    z.MonthlyLoad = np.zeros((12, 31))

    # Declare the daily values as ReDimensional arrays in addition
	# to Pesticide components
    z.DailyUplandSed = np.zeros((z.DimYrs, 12, 31))
    z.DailyUplandN = np.zeros((z.DimYrs, 12, 31))
    z.DailyUplandP = np.zeros((z.DimYrs, 12, 31))
    z.DailyTileDrainN = np.zeros((z.DimYrs, 12, 31))
    z.DailyTileDrainP = np.zeros((z.DimYrs, 12, 31))
    z.DailyStrmSed = np.zeros((z.DimYrs, 12, 31))
    z.DailySepticN = np.zeros((z.DimYrs, 12, 31))
    z.DailySepticP = np.zeros((z.DimYrs, 12, 31))
    z.DailyStrmN = np.zeros((z.DimYrs, 12, 31))
    z.DailyStrmP = np.zeros((z.DimYrs, 12, 31))
    z.DailyGroundN = np.zeros((z.DimYrs, 12, 31))
    z.DailyGroundP = np.zeros((z.DimYrs, 12, 31))
    z.DayGroundNitr = np.zeros((z.DimYrs, 12, 31))
    z.DayGroundPhos = np.zeros((z.DimYrs, 12, 31))
    z.DayDisPhos = np.zeros((z.DimYrs, 12, 31))
    z.DayDisNitr = np.zeros((z.DimYrs, 12, 31))
    z.DayTotNitr = np.zeros((z.DimYrs, 12, 31))
    z.DailyPointN = np.zeros((z.DimYrs, 12, 31))
    z.DailyPointP = np.zeros((z.DimYrs, 12, 31))
    z.DayTotPhos = np.zeros((z.DimYrs, 12, 31))
    z.DayLuTotN = np.zeros((16, z.DimYrs, 12, 31))
    z.DayLuTotP = np.zeros((16, z.DimYrs, 12, 31))
    z.DayLuDisN = np.zeros((16, z.DimYrs, 12, 31))
    z.DayLuDisP = np.zeros((16, z.DimYrs, 12, 31))
    z.DayPondNitr = np.zeros((12, 31))
    z.DayPondPhos = np.zeros((12, 31))
    z.DayNormNitr = np.zeros((12, 31))
    z.DayNormPhos = np.zeros((12, 31))
    z.WashImperv = np.zeros(16)
    z.NetSolidLoad = np.zeros(3)
    z.DayShortNitr = np.zeros((12, 31))
    z.DayShortPhos = np.zeros((12, 31))
    z.DayDischargeNitr = np.zeros((12, 31))
    z.DayDischargePhos = np.zeros((12, 31))
    z.DayErWashoff = np.zeros((16, z.DimYrs, 12, 31))
    z.Perc = np.zeros((z.DimYrs, 12, 31))
    z.DeepFlow = np.zeros((z.DimYrs, 12, 31))
    z.DayQRunoff = np.zeros((z.DimYrs, 12, 31))
    z.DaysYear = np.zeros(40)
    z.SdYld = np.zeros((z.DimYrs, 12, 31))
    z.Erosn = np.zeros((z.DimYrs, 12, 31))
    z.DayErosion = np.zeros((z.DimYrs, 12, 31))
    z.DayLuErosion = np.zeros((16, z.DimYrs, 12, 31))
    z.DaySed = np.zeros((z.DimYrs, 12, 31))
    z.DayLuSed = np.zeros((16, z.DimYrs, 12, 31))
    z.DayRunoff = np.zeros((z.DimYrs, 12, 31))
    z.DayLuRunoff = np.zeros((16, z.DimYrs, 12, 31))
    z.MeltPest = np.zeros((z.DimYrs, 12, 31))
    z.PrecPest = np.zeros((z.DimYrs, 12, 31))
    z.DailyGrFlow = np.zeros((z.DimYrs, 12, 31))
    z.PestAppMonth1 = np.zeros(16)
    z.PestAppYear1 = np.zeros(16)
    z.PestAppDate1 = np.zeros(16)
    z.PestAppMonth2 = np.zeros(16)
    z.PestAppYear2 = np.zeros(16)
    z.PestAppDate2 = np.zeros(16)
    z.PestShedName = np.zeros(12)
    z.PestCropArea = np.zeros(12)
    z.PestSoilBd = np.zeros(12)
    z.PestSoilAwc = np.zeros(12)
    z.PestSoilOm = np.zeros(12)
    z.PestCropName = np.zeros(12)
    z.PestName1 = np.zeros(16)
    z.PestRate1 = np.zeros(31)
    z.PestParamCarbon1 = np.zeros(16)
    z.PestParamWater1 = np.zeros(16)
    z.PestDecay1 = np.zeros(16)
    z.PestHalfLife1 = np.zeros(16)
    z.PestName2 = np.zeros(16)
    z.PestRate2 = np.zeros(31)
    z.PestParamCarbon2 = np.zeros(16)
    z.PestParamWater2 = np.zeros(16)
    z.PestDecay2 = np.zeros(16)
    z.PestHalfLife2 = np.zeros(16)
    z.DailyETCm = np.zeros((z.DimYrs, 12, 31))
    z.DailyETShal = np.zeros((z.DimYrs, 12, 31))
    z.PercCm = np.zeros((z.DimYrs, 12, 31))
    z.PercShal = np.zeros((z.DimYrs, 12, 31))
    z.DailyUnsatStorCm = np.zeros((z.DimYrs, 12, 31))
    z.DailyUnsatStorShal = np.zeros((z.DimYrs, 12, 31))
    z.DailyET = np.zeros((z.DimYrs, 12, 31))
    z.DailyRetent = np.zeros((z.DimYrs, 12, 31))
    z.SatStorPest = np.zeros((z.DimYrs, 12, 31))
    z.UrbanRunoff = np.zeros((z.DimYrs, 12))
    z.RuralRunoff = np.zeros((z.DimYrs, 12))
    z.DailyInfilt = np.zeros((z.DimYrs, 12, 31))
    z.StreamFlowVol = np.zeros((z.DimYrs, 12))
    z.DailyCN = np.zeros((z.DimYrs, 12, 31))
    z.DailyWater = np.zeros((z.DimYrs, 12, 31))
    z.LE = np.zeros((z.DimYrs, 12))
    z.StreamBankEros = np.zeros((z.DimYrs, 12))
    z.StreamBankN = np.zeros((z.DimYrs, 12))
    z.StreamBankP = np.zeros((z.DimYrs, 12))
    z.AvStreamBankEros = np.zeros(12)
    z.AvStreamBankN = np.zeros(12)
    z.AvStreamBankP = np.zeros(12)
    z.DailyAMC5 = np.zeros((z.DimYrs, 12, 31))
    z.CropPercent = np.zeros(12)
    z.MonthFlow = np.zeros((z.DimYrs, 12))
    z.LuGrFlow = np.zeros((16, z.DimYrs, 12, 31))
    z.LuDeepSeep = np.zeros((16, z.DimYrs, 12, 31))
    z.LuInfiltration = np.zeros((16, z.DimYrs, 12, 31))
    z.PestSoilAwcCm = np.zeros(12)
    z.PestTemp = np.zeros((z.DimYrs, 12, 31))
    z.PestPrec = np.zeros((z.DimYrs, 12, 31))

    # Tile Drainage and Flow Variables
    z.AvTileDrain = np.zeros(12)
    z.StreamWithdrawal = np.zeros(12)
    z.GroundWithdrawal = np.zeros(12)
    z.AvWithdrawal = np.zeros(12)
    z.AvTileDrainN = np.zeros(12)
    z.AvTileDrainP = np.zeros(12)
    z.AvTileDrainSed = np.zeros(12)
    z.AvPtSrcFlow = np.zeros(12)
    z.TileDrainN = np.zeros((z.DimYrs, 12))
    z.TileDrainP = np.zeros((z.DimYrs, 12))
    z.TileDrainSed = np.zeros((z.DimYrs, 12))
    z.TileDrain = np.zeros((z.DimYrs, 12))
    z.TileDrainRO = np.zeros((z.DimYrs, 12))
    z.TileDrainGW = np.zeros((z.DimYrs, 12))
    z.GwAgLE = np.zeros((z.DimYrs, 12))
    z.Withdrawal = np.zeros((z.DimYrs, 12))
    z.PtSrcFlow = np.zeros((z.DimYrs, 12))

    z.StreamFlow = np.zeros((z.DimYrs, 12))
    z.StreamFlowLE = np.zeros((z.DimYrs, 12))
    z.Precipitation = np.zeros((z.DimYrs, 12))
    z.Evapotrans = np.zeros((z.DimYrs, 12))
    z.GroundWatLE = np.zeros((z.DimYrs, 12))
    z.AgRunoff = np.zeros((z.DimYrs, 12))
    z.Runoff = np.zeros((z.DimYrs, 12))
    z.Erosion = np.zeros((z.DimYrs, 12))
    z.SedYield = np.zeros((z.DimYrs, 12))
    z.DaysMonth = np.zeros((z.DimYrs, 12))
    z.WxMonth = np.zeros((z.DimYrs, 12))
    z.WxYear = np.zeros((z.DimYrs, 12))
    z.GroundNitr = np.zeros((z.DimYrs, 12))
    z.GroundPhos = np.zeros((z.DimYrs, 12))
    z.DisNitr = np.zeros((z.DimYrs, 12))
    z.SepticN = np.zeros((z.DimYrs, 12))
    z.SepticP = np.zeros((z.DimYrs, 12))
    z.TotNitr = np.zeros((z.DimYrs, 12))
    z.DisPhos = np.zeros((z.DimYrs, 12))
    z.TotPhos = np.zeros((z.DimYrs, 12))
    z.LuRunoff = np.zeros((z.DimYrs, 16))
    z.LuErosion = np.zeros((z.DimYrs, 16))
    z.LuSedYield = np.zeros((z.DimYrs, 16))
    z.LuDisNitr = np.zeros((z.DimYrs, 16))
    z.LuTotNitr = np.zeros((z.DimYrs, 16))
    z.LuDisPhos = np.zeros((z.DimYrs, 16))
    z.LuTotPhos = np.zeros((z.DimYrs, 16))
    z.SedTrans = np.zeros((z.DimYrs, 16))
    z.SepticNitr = np.zeros(z.DimYrs)
    z.SepticPhos = np.zeros(z.DimYrs)

    # DIMENSION LOCAL SEPTIC SYSTEM MODEL ARRAYS
    z.MonthPondNitr = np.zeros(12)
    z.MonthPondPhos = np.zeros(12)
    z.MonthNormNitr = np.zeros(12)
    z.MonthShortNitr = np.zeros(12)
    z.MonthShortPhos = np.zeros(12)
    z.MonthDischargeNitr = np.zeros(12)
    z.MonthDischargePhos = np.zeros(12)

    # ANIMAL FEEDING OPERATIONS VARIABLES
    z.AnimalName = np.zeros(9)
    z.NumAnimals = np.zeros(9)
    z.GrazingAnimal = np.zeros(9)
    z.AnimalDailyN = np.zeros(9)
    z.AnimalDailyP = np.zeros(9)
    z.FCOrgsPerDay = np.zeros(9)
    z.AvgAnimalWt = np.zeros(9)
    z.DailyAnimalN = np.zeros((z.DimYrs, 12, 31))
    z.DailyAnimalP = np.zeros((z.DimYrs, 12, 31))

    z.Month = np.zeros(12)
    z.NGPctManApp = np.zeros(12)
    z.NGAppNRate = np.zeros(12)
    z.NGAppPRate = np.zeros(12)
    z.NGAppFCRate = np.zeros(12)
    z.NGPctSoilIncRate = np.zeros(12)
    z.NGBarnNRate = np.zeros(12)
    z.NGBarnPRate = np.zeros(12)
    z.NGBarnFCRate = np.zeros(12)

    z.PctGrazing = np.zeros(12)
    z.PctStreams = np.zeros(12)
    z.GrazingNRate = np.zeros(12)
    z.GrazingPRate = np.zeros(12)
    z.GrazingFCRate = np.zeros(12)
    z.GRPctManApp = np.zeros(12)
    z.GRAppNRate = np.zeros(12)
    z.GRAppPRate = np.zeros(12)
    z.GRAppFCRate = np.zeros(12)
    z.GRPctSoilIncRate = np.zeros(12)
    z.GRBarnNRate = np.zeros(12)
    z.GRBarnPRate = np.zeros(12)
    z.GRBarnFCRate = np.zeros(12)

    # Calculated Values for Animal Feeding Operations
    z.NGLoadN = np.zeros(9)
    z.NGLoadP = np.zeros(9)
    z.NGLoadFC = np.zeros(9)
    z.NGAccManAppN = np.zeros(12)
    z.NGAccManAppP = np.zeros(12)
    z.NGAccManAppFC = np.zeros(12)
    z.NGAppManN = np.zeros(12)
    z.NGInitBarnN = np.zeros(12)
    z.NGLostManN = np.zeros((z.DimYrs, 12))
    z.NGLostBarnN = np.zeros((z.DimYrs, 12))
    z.NGAppManP = np.zeros(12)
    z.NGInitBarnP = np.zeros(12)
    z.NGLostManP = np.zeros((z.DimYrs, 12))
    z.NGLostBarnP = np.zeros((z.DimYrs, 12))
    z.NGAppManFC = np.zeros(12)
    z.NGInitBarnFC = np.zeros(12)
    z.NGLostManFC = np.zeros((z.DimYrs, 12))
    z.NGLostBarnFC = np.zeros((z.DimYrs, 12))

    z.GRLoadN = np.zeros(9)
    z.GRLoadP = np.zeros(9)
    z.GRLoadFC = np.zeros(9)
    z.GRAccManAppN = np.zeros(12)
    z.GRAccManAppP = np.zeros(12)
    z.GRAccManAppFC = np.zeros(12)
    z.GRAppManN = np.zeros(12)
    z.GRInitBarnN = np.zeros(12)
    z.GRLostManN = np.zeros((z.DimYrs, 12))
    z.GRLostBarnN = np.zeros((z.DimYrs, 12))
    z.GRLossN = np.zeros((z.DimYrs, 12))
    z.GRAppManP = np.zeros(12)
    z.GRInitBarnP = np.zeros(12)
    z.GRLostManP = np.zeros((z.DimYrs, 12))
    z.GRLostBarnP = np.zeros((z.DimYrs, 12))
    z.GRLossP = np.zeros((z.DimYrs, 12))
    z.GRAppManFC = np.zeros(12)
    z.GRInitBarnFC = np.zeros(12)
    z.GRLostManFC = np.zeros((z.DimYrs, 12))
    z.GRLostBarnFC = np.zeros((z.DimYrs, 12))
    z.GRLossFC = np.zeros((z.DimYrs, 12))
    z.GrazingN = np.zeros(12)
    z.GrazingP = np.zeros(12)
    z.GrazingFC = np.zeros(12)
    z.GRStreamN = np.zeros(12)
    z.GRStreamP = np.zeros(12)
    z.GRStreamFC = np.zeros(12)
    z.LossFactAdj = np.zeros((z.DimYrs, 12))
    z.AnimalN = np.zeros((z.DimYrs, 12))
    z.AnimalP = np.zeros((z.DimYrs, 12))
    z.AnimalFC = np.zeros((z.DimYrs, 12))
    z.AvAnimalN = np.zeros(12)
    z.AvAnimalP = np.zeros(12)
    z.AvAnimalFC = np.zeros(12)
    z.AvWWOrgs = np.zeros(12)
    z.AvSSOrgs = np.zeros(12)
    z.AvUrbOrgs = np.zeros(12)
    z.AvWildOrgs = np.zeros(12)
    z.AvTotalOrgs = np.zeros(12)
    z.AvCMStream = np.zeros(12)
    z.AvOrgConc = np.zeros(12)
    z.WWOrgs = np.zeros((z.DimYrs, 12))
    z.SSOrgs = np.zeros((z.DimYrs, 12))
    z.UrbOrgs = np.zeros((z.DimYrs, 12))
    z.WildOrgs = np.zeros((z.DimYrs, 12))
    z.TotalOrgs = np.zeros((z.DimYrs, 12))
    z.CMStream = np.zeros((z.DimYrs, 12))
    z.OrgConc = np.zeros((z.DimYrs, 12))
    z.AvGRLostBarnN = np.zeros(12)
    z.AvGRLostBarnP = np.zeros(12)
    z.AvNGLostBarnN = np.zeros(12)
    z.AvNGLostBarnP = np.zeros(12)
    z.AvNGLostManP = np.zeros(12)
    z.AvNGLostBarnFC = np.zeros(12)
    z.AvGRLostBarnFC = np.zeros(12)

    # Initialize non-arrayed variables
    z.Nqual = 0
    z.q = 0
    z.k = 0
    z.BasinArea = 0
    z.Qretention = 0
    z.FilterEff = 0
    z.FilterWidth = 0
    z.OutFiltWidth = 0
    z.Capacity = 0
    z.BasinDeadStorage = 0
    z.DaysToDrain = 0
    z.CleanMon = 0
    z.Clean = 0
    z.CleanSwitch = 0
    z.OutletCoef = 0
    z.BasinVol = 0
    z.Volume = 0
    z.ActiveVol = 0
    z.DetentFlow = 0

     # If RunQual output is requested, then redim RunQual values
    PrelimQualCalculations.ReDimRunQualVars(z)

    # Set the Total AEU to the value from the Animal Density layer
    if VersionMatch(z.TranVersionNo, '1.[0-9].[0-9]'):
		for i in range(12):
			z.AnnDayHrs += z.DayHrs[i]

		for l in range(z.NRur):
            z.AreaTotal += z.Area[l]
            z.RurAreaTotal += z.Area[l]

		for l in range(z.NRur, z.NLU):
            z.AreaTotal += z.Area[l]
            z.UrbAreaTotal += z.Area[l]

        z.TotAreaMeters = z.AreaTotal * 10000

        # Get the area weighted average CN for rural areas
        z.AvCNRur = 0
		for l in range(z.NRur):
            # Calculate average area weighted CN and KF
            z.AvCNRur += z.CN[l] * z.Area[l] / z.RurAreaTotal

        # Get the area weighted average CN for urban areas
        z.AvCNUrb = 0
		for l in range(z.NRur, z.NLU):
            # Calculate average area-weighted CN for urban areas
	        if z.UrbAreaTotal > 0:
                z.AvCNUrb += (z.Imper[l] * z.CNI[2, l] +
                              (1 - z.Imper[l]) * z.CNP[2, l]) *
                              z.Area[l] / z.UrbAreaTotal

        # Calculate the average CN and percent urban area
        z.AvCN = (z.AvCNRur * z.RurAreaTotal / z.AreaTotal) + \
                 (z.AvCNUrb * z.UrbAreaTotal / z.AreaTotal)

        z.PcntUrbanArea = z.UrbAreaTotal / z.AreaTotal

        if z.SepticFlag is YesOrNo.YES:
            for i in range(12):
                z.SepticsDay[i] = z.NumNormalSys[i] + z.NumPondSys[i] + \
                                  z.NumShortSys[i] + z.NumDischargeSys[i]

        if VersionMatch(z.TranVersionNo, '1.[0-2].[0-9]'):
            z.Storm = 0
            z.CSNAreaSim = 0
            z.CSNDevType = "None"

        if VersionMatch(z.TranVersionNo, '1.[0-1].[0-9]'):
            for i in range(5):
                z.ISRR(i) = 0
                z.ISRA(i) = 0
            z.SweepType = 1
            z.UrbSweepFrac = 1
        elif VersionMatch(z.TranVersionNo, '1.[2-3].[0-9]'):
            z.SweepType = 1
            z.UrbSweepFrac = 1

        for i in range(12):
            if z.SweepType is SweepType.VACUUM:
                if z.StreetSweepNo[i] == 0: z.SweepFrac[i] = 1
                if z.StreetSweepNo[i] == 1: z.SweepFrac[i] = 0.94
                if z.StreetSweepNo[i] == 2: z.SweepFrac[i] = 0.89
                if z.StreetSweepNo[i] == 3: z.SweepFrac[i] = 0.84
                if z.StreetSweepNo[i] >= 4: z.SweepFrac[i] = 0.79
            else:
                z.SweepType = SweepType.MECHANICAL
                if z.StreetSweepNo[i] == 0: z.SweepFrac[i] = 1
                if z.StreetSweepNo[i] == 1: z.SweepFrac[i] = 0.99
                if z.StreetSweepNo[i] == 2: z.SweepFrac[i] = 0.98
                if z.StreetSweepNo[i] == 3: z.SweepFrac[i] = 0.97
                if z.StreetSweepNo[i] >= 4: z.SweepFrac[i] = 0.96

        # Get the Animal values
        z.InitGrN = 0
        z.InitGrP = 0
        z.InitGrFC = 0
        z.InitNgN = 0
        z.InitNgP = 0
        z.InitNgFC = 0

#        for a in range(9):
#            if z.GrazingAnimal[a] is YesOrNo.NO:
#                NGLoadN(a) = (NumAnimals(a) * AvgAnimalWt(a) / 1000) * AnimalDailyN(a) * 365
#                NGLoadP(a) = (NumAnimals(a) * AvgAnimalWt(a) / 1000) * AnimalDailyP(a) * 365
#                NGLoadFC(a) = (NumAnimals(a) * AvgAnimalWt(a) / 1000) * FCOrgsPerDay(a) * 365
#                InitNgN = InitNgN + NGLoadN(a)
#                InitNgP = InitNgP + NGLoadP(a)
#                InitNgFC = InitNgFC + NGLoadFC(a)
#            End If
#
#            If GrazingAnimal(a) = "Y" Then
#                GRLoadN(a) = (NumAnimals(a) * AvgAnimalWt(a) / 1000) * AnimalDailyN(a) * 365
#                GRLoadP(a) = (NumAnimals(a) * AvgAnimalWt(a) / 1000) * AnimalDailyP(a) * 365
#                GRLoadFC(a) = (NumAnimals(a) * AvgAnimalWt(a) / 1000) * FCOrgsPerDay(a) * 365
#                InitGrN = InitGrN + GRLoadN(a)
#                InitGrP = InitGrP + GRLoadP(a)
#                InitGrFC = InitGrFC + GRLoadFC(a)
#            End If
#        Next a
#
#        # Obtain AEU for each farm animal
#        AEU1 = ((NumAnimals(3) / 2) * (AvgAnimalWt(3)) / 1000) + ((NumAnimals(4) / 2) * (AvgAnimalWt(4)) / 1000)
#        AEU2 = (NumAnimals(8) * AvgAnimalWt(8)) / 1000
#        AEU3 = (NumAnimals(6) * AvgAnimalWt(6)) / 1000
#        AEU4 = (NumAnimals(5) * AvgAnimalWt(5)) / 1000
#        AEU5 = (NumAnimals(7) * AvgAnimalWt(7)) / 1000
#        AEU6 = (NumAnimals(1) * AvgAnimalWt(1)) / 1000
#        AEU7 = (NumAnimals(2) * AvgAnimalWt(2)) / 1000
#
#        # Get the total AEU, Total livestock and poultry AEU
#        TotAEU = (AEU1 + AEU2 + AEU3 + AEU4 + AEU5 + AEU6 + AEU7)
#        TotLAEU = (AEU3 + AEU4 + AEU5 + AEU6 + AEU7)
#        TotPAEU = (AEU1 + AEU2)
#
#        # Get the Non-Grazing Animal Worksheet values
#        For i = 1 To 12
#            Input #1, Month(i), NGPctManApp(i), NGAppNRate(i), NGAppPRate(i), NGAppFCRate(i), NGPctSoilIncRate(i), NGBarnNRate(i), NGBarnPRate(i), NGBarnFCRate(i)
#
#            # For Non-Grazing
#            NGAccManAppN(i) = NGAccManAppN(i) + (InitNgN / 12) - (NGPctManApp(i) * InitNgN)
#            If NGAccManAppN(i) < 0 Then NGAccManAppN(i) = 0
#
#            NGAccManAppP(i) = NGAccManAppP(i) + (InitNgP / 12) - (NGPctManApp(i) * InitNgP)
#            If NGAccManAppP(i) < 0 Then NGAccManAppP(i) = 0
#
#            NGAccManAppFC(i) = NGAccManAppFC(i) + (InitNgFC / 12) - (NGPctManApp(i) * InitNgFC)
#            If NGAccManAppFC(i) < 0 Then NGAccManAppFC(i) = 0
#
#            NGAppManN(i) = NGPctManApp(i) * InitNgN
#            NGInitBarnN(i) = NGAccManAppN(i) - NGAppManN(i)
#            If NGInitBarnN(i) < 0 Then NGInitBarnN(i) = 0
#
#            NGAppManP(i) = NGPctManApp(i) * InitNgP
#            NGInitBarnP(i) = NGAccManAppP(i) - NGAppManP(i)
#            If NGInitBarnP(i) < 0 Then NGInitBarnP(i) = 0
#
#            NGAppManFC(i) = NGPctManApp(i) * InitNgFC
#            NGInitBarnFC(i) = NGAccManAppFC(i) - NGAppManFC(i)
#            If NGInitBarnFC(i) < 0 Then NGInitBarnFC(i) = 0
#        Next i
#
#        # Read the Grazing Animal Worksheet values
#        For i = 1 To 12
#            Input #1, Month(i), PctGrazing(i), PctStreams(i), GrazingNRate(i), GrazingPRate(i), GrazingFCRate(i), GRPctManApp(i), GRAppNRate(i), GRAppPRate(i), GRAppFCRate(i), GRPctSoilIncRate(i), GRBarnNRate(i), GRBarnPRate(i), GRBarnFCRate(i)
#
#            GrazingN(i) = PctGrazing(i) * (InitGrN / 12)
#            GrazingP(i) = PctGrazing(i) * (InitGrP / 12)
#            GrazingFC(i) = PctGrazing(i) * (InitGrFC / 12)
#
#            GRStreamN(i) = PctStreams(i) * GrazingN(i)
#            GRStreamP(i) = PctStreams(i) * GrazingP(i)
#            GRStreamFC(i) = PctStreams(i) * GrazingFC(i)
#
#            # Get the annual sum for FC
#            AvGRStreamFC = AvGRStreamFC + GRStreamFC(i)
#            AvGRStreamN = AvGRStreamN + GRStreamN(i)
#            AvGRStreamP = AvGRStreamP + GRStreamP(i)
#
#            GRAccManAppN(i) = GRAccManAppN(i) + (InitGrN / 12) - (GRPctManApp(i) * InitGrN) - GrazingN(i)
#            If GRAccManAppN(i) < 0 Then GRAccManAppN(i) = 0
#
#            GRAccManAppP(i) = GRAccManAppP(i) + (InitGrP / 12) - (GRPctManApp(i) * InitGrP) - GrazingP(i)
#            If GRAccManAppP(i) < 0 Then GRAccManAppP(i) = 0
#
#            GRAccManAppFC(i) = GRAccManAppFC(i) + (InitGrFC / 12) - (GRPctManApp(i) * InitGrFC) - GrazingFC(i)
#            If GRAccManAppFC(i) < 0 Then GRAccManAppFC(i) = 0
#
#            GRAppManN(i) = GRPctManApp(i) * InitGrN
#            GRInitBarnN(i) = GRAccManAppN(i) - GRAppManN(i)
#            If GRInitBarnN(i) < 0 Then GRInitBarnN(i) = 0
#
#            GRAppManP(i) = GRPctManApp(i) * InitGrP
#            GRInitBarnP(i) = GRAccManAppP(i) - GRAppManP(i)
#            If GRInitBarnP(i) < 0 Then GRInitBarnP(i) = 0
#
#            GRAppManFC(i) = GRPctManApp(i) * InitGrFC
#            GRInitBarnFC(i) = GRAccManAppFC(i) - GRAppManFC(i)
#            If GRInitBarnFC(i) < 0 Then GRInitBarnFC(i) = 0
#        Next i
#
#        # Recalculate AEU using the TotAEU from the animal file and the total area of the basin in Acres
#        If TotLAEU > 0 Then
#            AEU = TotLAEU / (AreaTotal * 2.471)
#        Else
#            AEU = 0
#        End If
#
#        # Recalculate Sed A Factor using updated AEU value based on animal data
#        SedAFactor = ((0.00467 * PcntUrbanArea) + (0.000863 * AEU) + (0.000001 * AvCN) + (0.000425 * AvKF) + (0.000001 * AvSlope) - 0.000036) * SedAAdjust
#        If SedAFactor < 0.00001 Then
#            SedAFactor = 0.00001
#        End If
#
#        # Read the Load Delivery data
#        If TranVersionNo Like "1.0.[0-9]" Then
#            Input #1, ShedAreaDrainLake, RetentNLake, RetentPLake, RetentSedLake
#            AttenFlowDist = 0: AttenFlowVel = 0: AttenLossRateN = 0: AttenLossRateP = 0: AttenLossRateTSS = 0: AttenLossRatePath = 0: StreamFlowVolAdj = 1
#        Else
#            Input #1, ShedAreaDrainLake, RetentNLake, RetentPLake, RetentSedLake, AttenFlowDist, AttenFlowVel, AttenLossRateN, AttenLossRateP, AttenLossRateTSS, AttenLossRatePath, StreamFlowVolAdj
#        End If
#        If AttenFlowDist > 0 And AttenFlowVel > 0 Then
#            FlowDays = AttenFlowDist / (AttenFlowVel * 24)
#        Else
#            FlowDays = 0
#        End If
#        AttenN = FlowDays * AttenLossRateN
#        AttenP = FlowDays * AttenLossRateP
#        AttenTSS = FlowDays * AttenLossRateTSS
#        AttenPath = FlowDays * AttenLossRatePath
#        #MsgBox (AttenN & ", " & AttenP & ", " & AttenTSS & ", " & AttenPath)
#
#        # Read Weather data
#        YearStart = 1: YearEnd = 0: TotWxYrs = 0: CalYear = WxYrBeg
#        ReDim DaysMonth(WxYrs, 12), WxMonth(WxYrs, 12), WxYear(WxYrs, 12)
#        Done = False
#        For Y = 1 To WxYrs
#            CleanSwitch = 0
#            If Not Done Then
#                ReDim Temp(YearStart To WxYrs, 12, 31), Prec(YearStart To WxYrs, 12, 31), TempSum(YearStart To WxYrs, 12), TempMonth(YearStart To WxYrs, 12)
#                For Yr = YearStart To WxYrs
#                    For i = 1 To 12
#                        Input #1, DaysMonth(Yr, i), WxMonth(Yr, i), WxYear(Yr, i)
#                        For j = 1 To DaysMonth(Yr, i)
#                            Input #1, Temp(Yr, i, j), Prec(Yr, i, j)
#                        Next j
#                    Next i
#                    CalYear = WxYrBeg + Yr
#                Next Yr
#                Done = True
#            End If
#        Next Y
#
#        #Read Urban Area data
#        Input #1, NumUAs, UABasinArea
#        If NumUAs > 0 Then
#            ReDim UAId(NumUAs - 1), UAName(NumUAs - 1), UAArea(NumUAs - 1), UALU(NumUAs - 1, 17), UALUArea(NumUAs - 1, 17), UAfa(NumUAs - 1), UAfaAreaFrac(NumUAs - 1), UATD(NumUAs - 1), UATDAreaFrac(NumUAs - 1), UASB(NumUAs - 1), UASBAreaFrac(NumUAs - 1), UAGW(NumUAs - 1), UAGWAreaFrac(NumUAs - 1), UAPS(NumUAs - 1), UAPSAreaFrac(NumUAs - 1), UASS(NumUAs - 1), UASSAreaFrac(NumUAs - 1)
#            For ua = 0 To NumUAs - 1
#                Input #1, UAId(ua), UAName(ua), UAArea(ua)
#                SumUAId(ua) = UAId(ua)
#                For l = 0 To 16
#                    Input #1, UALU(ua, l), UALUArea(ua, l)
#                Next l
#                Input #1, UAfa(ua), UAfaAreaFrac(ua)
#                Input #1, UATD(ua), UATDAreaFrac(ua)
#                Input #1, UASB(ua), UASBAreaFrac(ua)
#                Input #1, UAGW(ua), UAGWAreaFrac(ua)
#                Input #1, UAPS(ua), UAPSAreaFrac(ua)
#                Input #1, UASS(ua), UASSAreaFrac(ua)
#            Next ua
#        End If
#        Close #1
#
#        # Calculate retention coefficients
#        RetentFactorN = (1 - (ShedAreaDrainLake * RetentNLake))
#        RetentFactorP = (1 - (ShedAreaDrainLake * RetentPLake))
#        RetentFactorSed = (1 - (ShedAreaDrainLake * RetentSedLake))
#	else:
#		raise Exception('Input data file is not in the correct format or is no longer supported')


def VersionMatch(TranVersionNo, VersionPatternRegex):
	return True
