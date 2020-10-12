#!/usr/bin/python

# permissions need to be 755 or more restrictive.
import cgi, sys, cgitb, csv, json

sys.stderr = sys.stdout # Make sure we can see any errors

cgitb.enable(display=0, logdir="pylogs")

data 						= cgi.FieldStorage()
fileName   					= data.getvalue("fileName", "FILENAME_NULL")
subjectkey	 				= data.getvalue("subjectkey", "GUID_NULL")
autoWorkerID 				= data.getvalue("autoWorkerID", "AUTOWORKERID_NULL")
interview_date 				= data.getvalue("interview_date", "INTERVIEWDATE_NULL")
interview_age 				= data.getvalue("interview_age", "INTERVIEWAGE_NULL")
sex 						= data.getvalue("sex", "SEX_NULL")
task_version 				= data.getvalue("task_version", "SEX_NULL")
excludedFileName   			= data.getvalue("excludedFileName", "EXCLUDEDFILENAME_NULL")
startDate					= data.getvalue("startDate", "STARTDATE_NULL")
endDate						= data.getvalue("endDate", "ENDDATE_NULL")
userAgentString 			= data.getvalue("userAgentString", "USERAGENTSTRING_NULL")
trialNums 					= json.loads(data.getvalue("trialNums", "TRIALNUMS_NULL"))
firstHalfProbabilities 		= json.loads(data.getvalue("firstHalfProbabilities", "FIRSTHALFPROBABILITIES_NULL"))
secondHalfProbabilities 	= json.loads(data.getvalue("secondHalfProbabilities", "SECONDHALFPROBABILITIES_NULL"))
deckColors 					= json.loads(data.getvalue("deckColors", "DECKCOLORS_NULL"))
deckPositions				= json.loads(data.getvalue("deckPositions", "DECKPOSITIONS_NULL"))
deckProbabilities			= json.loads(data.getvalue("deckProbabilities", "DECKPROBABILITIES_NULL"))
deckProbabilityOrder 		= json.loads(data.getvalue("deckProbabilityOrder", "DECKPROBABILITYORDER_NULL"))
colors 						= json.loads(data.getvalue("colors", "COLORS_NULL"))
keys 						= json.loads(data.getvalue("keys", "KEYS_NULL"))
positions 					= json.loads(data.getvalue("positions", "POSITIONS_NULL"))
probabilities 				= json.loads(data.getvalue("probabilities", "PROBABILITIES_NULL"))
results 					= json.loads(data.getvalue("results", "RESULTS_NULL"))
reversals 					= json.loads(data.getvalue("reversals", "REVERSALS_NULL"))
RT 							= json.loads(data.getvalue("RT", "RT_NULL"))
score 						= json.loads(data.getvalue("score", "SCORE_NULL"))
excludedReason 				= data.getvalue("excludedReason", "EXCLUDEDREASON_NULL")

if excludedReason != "NA":	
	fileName = excludedFileName

numRows = len(trialNums)
# Write to the file - XXX FIX BASED ON ROW INDEX
with open(fileName, 'a') as csvFile:
	csvWriter = csv.writer(csvFile, delimiter=",")

	for row in range(numRows):
		csvWriter.writerow('subjectkey', 'src_subject_id', 'interview_date', 'interview_age', 'sex', 'task_version', 'start_time', 'end_time', 'browser', 'trial', 'first_half_probabilities', 'second_half_probabilities', 'deck_color', 'deck_position', 'deck_probability_value_1', 'deck_probability_value_2', 'response_color', 'key_press', 'response_position', 'response_probability', 'reward', 'trial_type', 'rt', 'score', 'exclusion_reason')
		csvWriter.writerow([subjectkey, autoWorkerID, interview_date, interview_age, sex, task_version, startDate, endDate, userAgentString, trialNums[row],
			firstHalfProbabilities, secondHalfProbabilities, deckColors[row], deckPositions[row],
			deckProbabilities[row], deckProbabilityOrder[row], colors[row], keys[row], positions[row],
			probabilities[row], results[row], reversals[row], RT[row], score[row], excludedReason])

sys.stdout.write('Content-type: text/plain; charset=UTF-8\n\n')
sys.stdout.write('Done.')

