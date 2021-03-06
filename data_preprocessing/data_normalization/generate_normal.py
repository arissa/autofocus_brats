import sys
import normalizationModule
import os
import pdb

testf = open('/data2/arissa/Autofocus-Layer/test_brats2015nii_list.txt', 'r')
test_dir = testf.readlines()
for i in range(int(len(test_dir))):
    print("image" + str(i))
	
    ## MUST CHANGE STEP SIZE IF NORMALIZING TEST VS TRAIN
#     if i % 5 == 4:
#         continue
    step = 4
    direct_mask,_ = test_dir[step * int(i/step)].split("\n")    
    direct_image,_ = test_dir[i].split("\n")    
    direct_mask = direct_mask + "/mask.nii.gz"
    direct_image = direct_image +".gz"
    
#     pathToMainFolderWithSubjects = "./HGG_full/"
    pathToMainFolderWithSubjects = None
#     subjectsToProcess = os.listdir(pathToMainFolderWithSubjects)
#     subjectsToProcess.sort()
    ## i figured out that subjectsToProcess doesn't actually do anything
    subjectsToProcess = None
 
    saveOutput = True
    prefixToAddToOutp = "_zNorm2StdsMu"
     
    dtypeToSaveOutput = "float32"
    saveNormalizationPlots = True
         

    lowHighCutoffPercentile = [5., 95.]
    lowHighCutoffTimesTheStd = [3., 3.]
    cutoffAtWholeImgMean = True 
    print(direct_image)
    print(direct_mask)
    normalizationModule.do_normalization( __file__,
				pathToMainFolderWithSubjects,
				subjectsToProcess,
				direct_image,direct_mask,				
				saveOutput,
				prefixToAddToOutp,				
				dtypeToSaveOutput,
				saveNormalizationPlots,								
				lowHighCutoffPercentile, # Can be None
				lowHighCutoffTimesTheStd, # Can be None
				cutoffAtWholeImgMean,
				)
#     break



