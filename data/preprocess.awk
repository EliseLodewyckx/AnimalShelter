function replaceEmptyWithUnknown(Input) {
	if(length(Input) == 0) {
		return "Unknown"
	}
	return Input
}

function defineIntact(SexuponOutcome) {
	SexuponOutcome = replaceEmptyWithUnknown(SexuponOutcome)
	if (match(SexuponOutcome,"Intact")) {
                Intact="Intact"
        }
        else if (match(SexuponOutcome,"Unknown")) {
                Intact="Unknown"
        } else {
                Intact="Non-intact"
        }
	return Intact
}

function defineSex(SexuponOutcome) {
	SexuponOutcome = replaceEmptyWithUnknown(SexuponOutcome)
	if(match(SexuponOutcome,"Female")) {
		Sex="Female"
	} else if (match(SexuponOutcome,"Unknown")) {
		Sex="Unknown"
	} else {
		Sex="Male"
	}
	return Sex
}

function defineAgeNumber(AgeuponOutcome) {
	AgeuponOutcome = replaceEmptyWithUnknown(AgeuponOutcome)
	if (match(AgeuponOutcome,"Unknown")) {
		AgeNumber="Unknown"
	} else {
		split(AgeuponOutcome, splitage, " ")
		AgeNumber=splitage[1]
	}
	return AgeNumber
}

function defineAgeType(AgeuponOutcome) {
	AgeuponOutcome = replaceEmptyWithUnknown(AgeuponOutcome)
	if (match(Ageuponoutcome, "Unknown")) {
		AgeType = "Unknown"
	} else {
		split(AgeuponOutcome, splitage," ")
		AgeType=splitage[2]
	}
	return AgeType
}

function defineNormalizedAgeType(AgeType) {
	if(match(AgeType,/.*s$/)) {
		AgeTypeNormalized =substr(AgeType,0,length(AgeType)-1)
	} else {
		AgeTypeNormalized = AgeType
	}
	return AgeTypeNormalized
} 

function defineAgeInYears(AgeNumber, AgeTypeNormalized) {
	switch (AgeTypeNormalized) {
	case "day":
		AgeInYears = AgeNumber / 365.25
		break
	case "week":
		AgeInYears = AgeNumber / 52
		break
	case "month":
		AgeInYears = AgeNumber / 12
		break
	case "year":
		AgeInYears = AgeNumber
		break
	default:
		AgeInYears = "Unknown"
		break
	}
	return AgeInYears
}

function defineMix(Breed) {
	Breed = replaceEmptyWithUnknown(Breed)
	if(match(Breed, "Unknown")) {
		Mix = "Unknown"
	} else if(match(Breed, "Mix")) {
		Mix = "TRUE"
	} else {
		Mix = "FALSE"
	}
	return Mix	
}

BEGIN {
	FS=","
	
	print "OutcomeType;AnimalType;SexuponOutcome;Sex;Intact;AgeNumber;AgeType;AgeTypeNormalized;AgeInYears;Breed;Mix;Color"
}
{
	OutcomeType=$4
	OutcomeSubtype=$5
	AnimalType=$6
	SexuponOutcome=$7
	Sex=defineSex(SexuponOutcome)
	Intact=defineIntact(SexuponOutcome)
	AgeuponOutcome=$8
	AgeNumber=defineAgeNumber(AgeuponOutcome)
	AgeType=defineAgeType(AgeuponOutcome)
	AgeTypeNormalized=defineNormalizedAgeType(defineAgeType(AgeuponOutcome))
	AgeInYears=defineAgeInYears(AgeNumber, AgeTypeNormalized)
	Breed=$9
	Mix=defineMix(Breed)
	Color=$10

	if (NR != 1) {
		print OutcomeType ";" AnimalType ";" SexuponOutcome ";" Sex ";" Intact ";" AgeNumber ";" AgeType ";" AgeTypeNormalized ";" AgeInYears ";" Breed ";" Mix ";" Color
	}
}
