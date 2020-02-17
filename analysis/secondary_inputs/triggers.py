###
# From https://github.com/bu-cms/bucoffea/blob/master/bucoffea/config/monojet.yaml
# Trigger scale factors taken from https://github.com/bu-cms/bucoffea/tree/master/bucoffea/data/sf/trigger
# Egamma triggers follow the POG recommendations here https://twiki.cern.ch/twiki/bin/view/CMS/EgHLTRunIISummary
###

from coffea.util import save

met_trigger_paths = {}
met_trigger_paths["2016"] = ["HLT_PFMETNoMu90_PFMHTNoMu90_IDTight",
                             "HLT_PFMETNoMu100_PFMHTNoMu100_IDTight",
                             "HLT_PFMETNoMu110_PFMHTNoMu110_IDTight",
                             "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight"]
met_trigger_paths["2017"] = ["HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60",
                             "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight"]
met_trigger_paths["2018"] = ["HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60",
                             "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight"]

singleele_trigger_paths = {}
singleele_trigger_paths["2016"] = ["HLT_Ele27_WPTight_Gsf",
                                   "HLT_Ele115_CaloIdVT_GsfTrkIdT",
                                   "HLT_Photon175"]
singleele_trigger_paths["2017"] = ["HLT_Ele35_WPTight_Gsf",
                                   "HLT_Ele115_CaloIdVT_GsfTrkIdT",
                                   "HLT_Photon200"]
singleele_trigger_paths["2018"] = ["HLT_Ele32_WPTight_Gsf",
                                   "HLT_Ele115_CaloIdVT_GsfTrkIdT",
                                   "HLT_Photon200"]

singlepho_trigger_paths = {}
singlepho_trigger_paths["2016"] = ["HLT_Photon175",
                                   "HLT_Photon165_HE10"]
singlepho_trigger_paths["2017"] = ["HLT_Photon200"]
singlepho_trigger_paths["2018"] = ["HLT_Photon200"]

triggers = {}
triggers['met_trigger_paths']       = met_trigger_paths
triggers['singleele_trigger_paths'] = singleele_trigger_paths
triggers['singlepho_trigger_paths'] = singlepho_trigger_paths
save(triggers, 'secondary_inputs/triggers.coffea')
