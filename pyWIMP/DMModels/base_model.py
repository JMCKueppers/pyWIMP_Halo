import ROOT

class BaseVariables:
    class_tag = 0 
    def __init__(self, \
                 time_beginning,\
                 time_in_years,\
                 energy_threshold,\
                 energy_max,
                 use_tag = True,
                 time_offset=-61./365.25):  #default set offset so that amplitude modulation starts on Jan 1

        tag = ""
        if use_tag: tag = str(self.get_tag())
        self.time = ROOT.RooRealVar("time%s" % tag, "Time",time_beginning,\
                    time_in_years, "years") 
 
        self.ee_energy = ROOT.RooRealVar("ee_energy%s" % tag, "Energy", \
                         energy_threshold, energy_max, "keV")

        self.weighting = ROOT.RooRealVar("weight%s" % tag, "Weight", \
                         0, 1e15)
                         
        self.time_offset =  ROOT.RooRealVar("toffset%s" % tag, "Offset", \
                            time_offset, "years")
    @classmethod
    def get_tag(cls):
        cls.class_tag += 1
        return cls.class_tag

    def get_energy(self):
        return self.ee_energy

    def get_time(self):
        return self.time
    
    def get_time_offset(self):
          return self.time_offset
            
    def get_weighting(self):
        return self.weighting

    def set_energy(self, energy):
        self.ee_energy = energy

    def set_time(self, time):
        self.time = time

    def set_time_offset(self, time):
        self.time = time_offset

    def set_weighting(self, weighting):
        self.weighting = weighting

class BaseModel:
    class_tag = 0 
    class_use_tag = False
    def __init__(self,
                 basevars):
        self.basevars = basevars

    @classmethod
    def use_tag(cls, use_it = True):
        cls.class_use_tag = use_it 

    @classmethod
    def get_tag(cls):
        if not cls.class_use_tag: return "" 
        cls.class_tag += 1
        return str(cls.class_tag)
