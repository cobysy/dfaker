import random
import common_fields
import tools

def settings(start_time, params):
    settings_data = []
    settings = {}
    time_in_seconds = int(start_time.strftime('%s'))
    settings = common_fields.add_common_fields('settings', settings, time_in_seconds, params)
    settings["activeSchedule"] = "standard"
    settings["basalSchedules"] =  {"standard": [{"rate": 0.9, "start": 0},
                                                {"rate": 0.6, "start": 3600000},
                                                {"rate": 0.65, "start": 10800000},
                                                {"rate": 0.8, "start": 14400000},
                                                {"rate": 0.85, "start": 18000000},
                                                {"rate": 0.8, "start": 28800000},
                                                {"rate": 0.75, "start": 32400000},
                                                {"rate": 0.8, "start": 54000000},
                                                {"rate": 0.85, "start": 61200000}]}
    bgTarget_low = random.randrange(80, 120, 10)
    bgTarget_high = random.randrange(bgTarget_low, 140, 10)
    settings["bgTarget"] = [{"high": tools.convert_to_mmol(bgTarget_high), 
                             "low": tools.convert_to_mmol(bgTarget_low), 
                             "start": 0}]
    settings["carbRatio"] = [ {"amount": random.randint(9, 15), "start": 0}]
    settings["insulinSensitivity"] = [{"amount": tools.convert_to_mmol(50), "start": 0}]
    settings["units"] = { "bg": "mg/dL","carb": "grams"}
    settings_data.append(settings)
    return settings_data