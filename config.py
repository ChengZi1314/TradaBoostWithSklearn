
# set the path-to-files
TRAIN_FILE = "../dataTransfer/trainSample.csv"
TEST_FILE = "../dataTransfer/tSample.csv"

SUB_DIR = "./output"


NUM_SPLITS = 3
RANDOM_SEED = 2017

# types of columns of the dataset dataframe
CATEGORICAL_COLS = [
    "certtype", "country", "nationality", "politicalface", "marriage", "unitkind", "occupation",
    "position", "eduexperience", "edudegree", "financebelong", "creditlevel", "incomesource", "countrycode",
    "staff", "creditfarmer", "headship", "familystatus", "tempsaveflag", "isfarm", "certtype1",
    "isresident", "existscreditdetail", "havepboccard", "mod", "pbocaccstatus", "pboceducation",
    "pbocloan24mrepaystatus", "pbocmaxguaranteecategory5", "pbocmaxguarcategory5", "pbocmaxloancategory5"
]

NUMERIC_COLS = [
    'sex', 'balancesheet', 'familymonthincome', 'yearincome', 'mounthexpense', 'ods_date', 'part_date',
    'pboc1moncardapply', 'pboc1monloanapply', 'pboc24malloverdueloannum', 'pboc3moncardapply', 'pboc3monloanapply',
    'pboc6moncardapply', 'pboc6moncardusedamount', 'pboc6moncardusedrate', 'pboc6monloanapply',
    'pboc6monloanshouldrepay', 'pbocadministrationpunishnum', 'pbocage', 'pbocallccmaxoverduenum',
    'pbocallcredit6mminquotarate', 'pbocallhousegjjloannum', 'pbocassetsdisposal', 'pbocassetsdisposal_new',
    'pbocassetsdisposalnum', 'pbocavg6monthquota', 'pbocbaddebt', 'pbocbaddebt_new', 'pbocbaddebtnum',
    'pbocbadguaranteestatusnum', 'pbocbadloanamount', 'pbocbankcreditnum', 'pboccardlegalperson', 'pboccardmaxoverdue',
    'pboccardmaxoverduenum', 'pboccardminrepay', 'pboccardnum', 'pboccardoverdue', 'pboccardoverduenum',
    'pboccardrepay', 'pboccardshouldrepay', 'pboccardstate', 'pboccardusedamount', 'pboccarloannum', 'pboccarloanrepay',
    'pboccarloanrepayment', 'pboccarloanunclearednum', 'pboccc12mmaxoverduenum', 'pboccc12mmoverduenum',
    'pboccc12msoverduenum', 'pboccc12msumoverduenum', 'pboccc24mmaxoverduenum', 'pboccc24mmoverduenum',
    'pboccc24msoverduenum', 'pboccc24msumoverduenum', 'pboccc6mavgusedrate', 'pboccc6mmaxoverduenum',
    'pboccc6mmoverduenum', 'pboccc6msoverduenum', 'pboccc6msumoverduenum', 'pboccc6muserate',
    'pbocccclose12mmoverduemoney', 'pbocccclose12mmoverduenum', 'pbocccclose24mmoverduemoney',
    'pbocccclose24mmoverduenum', 'pbocccclose6mmoverduemoney', 'pbocccclose6mmoverduenum', 'pboccccurrabnormal',
    'pboccccurroverdueamount', 'pbocccopen12mmoverduenum', 'pbocccopen24mmoverduenum', 'pbocccopen6mmoverduenum',
    'pbocccoutaccountnum', 'pbocccrateover80account', 'pboccctotalamount', 'pboccctotalnum', 'pbocconsumerloancount',
    'pboccredit1mqueryrecordnum', 'pboccredit24mabnormal', 'pboccredit24mm2overduenum', 'pboccredit24mmaxoverduenum',
    'pboccredit24msumoverduenum', 'pboccredit25_60mmaxoverduenum', 'pboccredit25_60msumoverduenum',
    'pboccredit3mmaxoverduenum', 'pboccredit3moverduenum', 'pboccredit3mqueryrecordnum', 'pboccredit6mavgusedrate',
    'pboccredit6mm2overduenum', 'pboccredit6mmaxoverduenum', 'pboccredit6mqueryrecordnum', 'pboccredit6msumoverduenum',
    'pboccreditbadstatusaccountnum', 'pboccreditgaccountnum', 'pboccredithouseloandate1', 'pboccredithouseloandate2',
    'pboccredithouseloandate3', 'pboccredithouseloandate4', 'pboccredithouseloandate5', 'pboccreditloan12moverduenum',
    'pboccreditloan24mmaxoverduenum', 'pboccreditloan2mqueryrecordnum', 'pboccreditloan3mqueryrecordnum',
    'pboccreditloan6mavgusedrate', 'pboccreditloan6moverduenum', 'pboccreditloanhistory', 'pboccreditoverduemoney',
    'pboccredittotalnum', 'pboccredittradetype', 'pboccreditusedsum', 'pbocdifqueryorg12ca', 'pbocdifqueryorg12pla',
    'pbocdifqueryorg6ca', 'pbocdigitalinterpretation', 'pbocearliestqueryreason', 'pbocelsestudentandfarmerloan',
    'pbocfarmerloan', 'pbocforcerecordnum', 'pbocgjirate', 'pbocgjjamount', 'pbocguaranteeamount', 'pbocguaranteeanum',
    'pbocguaranteeremain', 'pbocguaranteerepay', 'pbocguarcurrabnormal', 'pbochouseloan6monthmoney',
    'pbochouseloanamount1', 'pbochouseloanamount2', 'pbochouseloanamount3', 'pbochouseloanamount4',
    'pbochouseloanamount5', 'pbochouseloancount', 'pbochouseloanmonthmoney', 'pbochouseloannum', 'pbochouseloannumall',
    'pbochouseloanrepay', 'pbochouseloanrepayment', 'pbochouseloanrepaymonthnum', 'pbocindustry', 'pbociscredit',
    'pbociscredithouseloan', 'pbocisexcute', 'pboclcurrlendernum', 'pboclcurroverdue', 'pbocloan12mm2overduenum',
    'pbocloan12mmaxoverduenum', 'pbocloan12mmoverduenum', 'pbocloan12mquerynum', 'pbocloan12msoverduenum',
    'pbocloan12msumoverduenum', 'pbocloan24mm2overduenum', 'pbocloan24mmaxoverduenum', 'pbocloan24mmoverduenum',
    'pbocloan24msoverduenum', 'pbocloan24msumoverduenum', 'pbocloan25_60mmaxduenum', 'pbocloan25_60msumduenum',
    'pbocloan2mquerynum', 'pbocloan3mmaxmortduenum', 'pbocloan3mmaxoverduenum', 'pbocloan3mquerynum',
    'pbocloan3msummortduenum', 'pbocloan3msumoverduenum', 'pbocloan6mmaxoverduenum', 'pbocloan6mmaxunmortduenum',
    'pbocloan6mmoverduenum', 'pbocloan6mquerynum', 'pbocloan6mqueryrecordnum', 'pbocloan6msoverduenum',
    'pbocloan6msumoverduenum', 'pbocloan6msumunmortduenum', 'pbocloanabnormalpaylastmonth',
    'pbocloanbadstatusaccountnum', 'pbocloancardusedrate', 'pbocloancurrabnormal', 'pbocloancurrbanlance',
    'pbocloancurrlendercount', 'pbocloancurrlendernum', 'pbocloancurroverdue', 'pbocloanextendlastmonth',
    'pbocloanguarantee', 'pbocloanguaranteenum', 'pbocloanguaranteeremin', 'pbocloanmaxoverdue',
    'pbocloanmaxoverduenum', 'pbocloanmonthdebt', 'pbocloanmonthsum', 'pbocloanmortunpaybalance',
    'pbocloanmortunpaynum', 'pbocloannotengagemonthsum', 'pbocloannothousemonthsum', 'pbocloanotherlastmonth',
    'pbocloanoverdue', 'pbocloanoverduenum', 'pbocloanoverduenumnew', 'pbocloanstate', 'pbocloantradetype',
    'pbocloanxdamount', 'pbocloanxdlastmonth', 'pbocloanxdmoney', 'pbocloanxdsummoney', 'pbocmaxcardamount',
    'pbocmaxdelq24mnum', 'pbocminaging', 'pbocmincreditcardmoney', 'pbocminhouseloanage', 'pbocminrepayaccountnum',
    'pbocmortgagecount', 'pbocnodelq12mnum', 'pbocnodelq6mnum', 'pbocnohousprovidentblance', 'pbocnononmortuncld',
    'pbocoutstandingloancount', 'pbocpctm1delq12mrate', 'pbocpersonalloannum', 'pbocprofession', 'pbocquerysumnum',
    'pbocquotarateover80account', 'pbocrelativeposition', 'pbocsemicmaxover180debt', 'pbocsemicredit12mm4overduenum',
    'pbocsemicredit12mmaxoverduenum', 'pbocsemicreditover180debt', 'pbocstudentloan', 'pbocsumcardamount',
    'pboctotalcredit', 'pbocunfinishedpayloan', 'pbocunhousegjjloannum', 'pboczh12monm1', 'pboczh12monm2',
    'pboczh12monm3', 'pboczh12monm4', 'pboczh12monm5', 'pboczh12monm6', 'pboczh12monm7', 'pboczh12monmax',
    'pboczh12monn', 'pboczh1mon', 'pboczh24mon', 'pboczh24monm1', 'pboczh24monm2', 'pboczh24monm3', 'pboczh24monm4',
    'pboczh24monm5', 'pboczh24monm6', 'pboczh24monm7', 'pboczh24monmax', 'pboczh2mon', 'pboczh3mon',
    'pboczh3monoverduenum', 'pboczh6monm1', 'pboczh6monm2', 'pboczh6monm3', 'pboczh6monm4', 'pboczh6monm5',
    'pboczh6monm6', 'pboczh6monm7', 'pboczh6monn', 'pboczhcard12monm1', 'pboczhcard12monm2', 'pboczhcard12monm3',
    'pboczhcard12monm4', 'pboczhcard12monm5', 'pboczhcard12monm6', 'pboczhcard12monm7', 'pboczhcard12monn',
    'pboczhcard24monm1', 'pboczhcard24monm2', 'pboczhcard24monm3', 'pboczhcard24monm4', 'pboczhcard24monm5',
    'pboczhcard24monm6', 'pboczhcard24monm7', 'pboczhcard24monmax', 'pboczhcard6monm1', 'pboczhcard6monm2',
    'pboczhcard6monm3', 'pboczhcard6monm4', 'pboczhcard6monm5', 'pboczhcard6monm6', 'pboczhcard6monm7',
    'pboczhloan12monm1', 'pboczhloan12monm2', 'pboczhloan12monm3', 'pboczhloan12monm4', 'pboczhloan12monm5',
    'pboczhloan12monm6', 'pboczhloan12monm7', 'pboczhloan12monn', 'pboczhloan24monm1', 'pboczhloan24monm2',
    'pboczhloan24monm3', 'pboczhloan24monm4', 'pboczhloan24monm5', 'pboczhloan24monm6', 'pboczhloan24monm7',
    'pboczhloan24monmax', 'pboczhloan6monm1', 'pboczhloan6monm2', 'pboczhloan6monm3', 'pboczhloan6monm4',
    'pboczhloan6monm5', 'pboczhloan6monm6', 'queryresult', 'queryresultmsg', 'relationuser', 'reportno',
    'semicard180dayoverdue', 'server_id', 'serviceid', 'sumpbocloanguarantee', 'sumpbocloanguaranteenum',
    'sumpbocloanguaranteeremin'
]

IGNORE_COLS = [
    "customerid", "target",
    "reportno", "balancesheet"
]
