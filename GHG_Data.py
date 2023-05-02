import pandas as pd

#%% 
#Importing ghg and intl agreement data, renaming column names
ghg_data = pd.read_csv('per-capita-ghg-emissions.csv')
gdp_data = pd.read_csv('GDP.csv')
gain_data = pd.read_csv('gain.csv')
#%% 
# Renaming columns for for consistency in other datasets 
ghg_data_names = {
                    'Entity': 'Name',
                    'Code': 'ISO3',
                    'Greenhouse gas emissions per person': 'Per_Capita_GHG_Emissions(tons)'
                    }
ghg_data = ghg_data.rename(columns=ghg_data_names)

# Dropping non-country level data (world, OECD, EU, etc.)
ghg_data = ghg_data.dropna(subset=['ISO3'])
gdp_data = gdp_data.dropna(subset=['ISO3'])
gain_data = gain_data.dropna(subset=['ISO3'])

gdp_data_panel = pd.melt(gdp_data, id_vars=['Name', 'ISO3'], var_name='Year', value_name='gdp_data_value')
gain_data_panel = pd.melt(gain_data, id_vars=['Name', 'ISO3'], var_name='Year', value_name='gdp_data_value')


#%% Import readiness, column names to years, convert to panel data

reliable_water = pd.read_csv('ID_WATE_06_ReliableDrinkingWater.csv')
reliable_water_names = {
                'reliable water 1995': '1995',
                'reliable water 1996': '1996',
                'reliable water 1997': '1997',
                'reliable water 1998': '1998',
                'reliable water 1999': '1999',
                'reliable water 2000': '2000',
                'reliable water 2001': '2001',
                'reliable water 2002': '2002',
                'reliable water 2003': '2003',
                'reliable water 2004': '2004',
                'reliable water 2005': '2005',
                'reliable water 2006': '2006',
                'reliable water 2007': '2007',
                'reliable water 2008': '2008',
                'reliable water 2009': '2009',
                'reliable water 2010': '2010',
                'reliable water 2011': '2011',
                'reliable water 2012': '2012',
                'reliable water 2013': '2013',
                'reliable water 2014': '2014',
                'reliable water 2015': '2015',
                'reliable water 2016': '2016',
                'reliable water 2017': '2017',
                'reliable water 2018': '2018',
                'reliable water 2019': '2019',
                'reliable water 2020': '2020',
                'Value': 'reliable_water_value'
                }
reliablewater = reliable_water.rename(columns=reliable_water_names)
reliable_water_panel = pd.melt(reliable_water, id_vars=['Name', 'ISO3'], var_name='Year', value_name='reliable_water_value')
#readiness_panel.to_csv('readiness_panel.csv')
#%% 
# Import score, column names to years, convert to panel data

dam_cap = pd.read_csv('ID_WATE_05_DamCap.csv')
dam_cap_names = {
                'Dam Capacity 1995': '1995',
                'Dam Capacity 1996': '1996',
                'Dam Capacity 1997': '1997',
                'Dam Capacity 1998': '1998',
                'Dam Capacity 1999': '1999',
                'Dam Capacity 2000': '2000',
                'Dam Capacity 2001': '2001',
                'Dam Capacity 2002': '2002',
                'Dam Capacity 2003': '2003',
                'Dam Capacity 2004': '2004',
                'Dam Capacity 2005': '2005',
                'Dam Capacity 2006': '2006',
                'Dam Capacity 2007': '2007',
                'Dam Capacity 2008': '2008',
                'Dam Capacity 2009': '2009',
                'Dam Capacity 2010': '2010',
                'Dam Capacity 2011': '2011',
                'Dam Capacity 2012': '2012',
                'Dam Capacity 2013': '2013',
                'Dam Capacity 2014': '2014',
                'Dam Capacity 2015': '2015',
                'Dam Capacity 2016': '2016',
                'Dam Capacity 2017': '2017',
                'Dam Capacity 2018': '2018',
                'Dam Capacity 2019': '2019',
                'Dam Capacity 2020': '2020',
                'Value': 'dam_cap_value'
                }

dam_cap = dam_cap.rename(columns=dam_cap_names)
dam_cap_panel = pd.melt(dam_cap, id_vars=['Name', 'ISO3'], var_name='Year', value_name='dam_cap_value')
#gain_panel.to_csv('gain_panel.csv')

#%% 
# 
#Import vulnerability score, column names to years, convert  to panel data

h20_withdrawal = pd.read_csv('ID_WATE_03_FreshH20Withdrawl.csv')
h20_withdrawal_names = {
                'h20 withdrawal 1995': '1995',
                'h20 withdrawal 1996': '1996',
                'h20 withdrawal 1997': '1997',
                'h20 withdrawal 1998': '1998',
                'h20 withdrawal 1999': '1999',
                'h20 withdrawal 2000': '2000',
                'h20 withdrawal 2001': '2001',
                'h20 withdrawal 2002': '2002',
                'h20 withdrawal 2003': '2003',
                'h20 withdrawal 2004': '2004',
                'h20 withdrawal 2005': '2005',
                'h20 withdrawal 2006': '2006',
                'h20 withdrawal 2007': '2007',
                'h20 withdrawal 2008': '2008',
                'h20 withdrawal 2009': '2009',
                'h20 withdrawal 2010': '2010',
                'h20 withdrawal 2011': '2011',
                'h20 withdrawal 2012': '2012',
                'h20 withdrawal 2013': '2013',
                'h20 withdrawal 2014': '2014',
                'h20 withdrawal 2015': '2015',
                'h20 withdrawal 2016': '2016',
                'h20 withdrawal 2017': '2017',
                'h20 withdrawal 2018': '2018',
                'h20 withdrawal 2019': '2019',
                'h20 withdrawal 2020': '2020',
                'Value': 'h20_withdrawal_value'
                }

h20_withdrawal = h20_withdrawal.rename(columns=h20_withdrawal_names)
h20_withdrawal_panel = pd.melt(h20_withdrawal, id_vars=['Name', 'ISO3'], var_name='Year', value_name='h20_withdrawal_value')
#vuln_panel.to_csv('vuln_panel.csv')
#%% 
electric_access = pd.read_csv('ID_INFR_06_ElectricityAccess.csv')
electric_access_names = {
                'electric access 1995': '1995',
                'electric access 1996': '1996',
                'electric access 1997': '1997',
                'electric access 1998': '1998',
                'electric access 1999': '1999',
                'electric access 2000': '2000',
                'electric access 2001': '2001',
                'electric access 2002': '2002',
                'electric access 2003': '2003',
                'electric access 2004': '2004',
                'electric access 2005': '2005',
                'electric access 2006': '2006',
                'electric access 2007': '2007',
                'electric access 2008': '2008',
                'electric access 2009': '2009',
                'electric access 2010': '2010',
                'electric access 2011': '2011',
                'electric access 2012': '2012',
                'electric access 2013': '2013',
                'electric access 2014': '2014',
                'electric access 2015': '2015',
                'electric access 2016': '2016',
                'electric access 2017': '2017',
                'electric access 2018': '2018',
                'electric access 2019': '2019',
                'electric access 2020': '2020',
                'Value': 'electric_access_value'
                }

electric_access = electric_access.rename(columns=electric_access_names)
electric_access_panel = pd.melt(electric_access, id_vars=['Name', 'ISO3'], var_name='Year', value_name='electric_access_value')
#%% 

disaster_prep = pd.read_csv('ID_INFR_05_DisasterPrep.csv')
disaster_prep_names = {
                'disaster prep 1995': '1995',
                'disaster prep 1996': '1996',
                'disaster prep 1997': '1997',
                'disaster prep 1998': '1998',
                'disaster prep 1999': '1999',
                'disaster prep 2000': '2000',
                'disaster prep 2001': '2001',
                'disaster prep 2002': '2002',
                'disaster prep 2003': '2003',
                'disaster prep 2004': '2004',
                'disaster prep 2005': '2005',
                'disaster prep 2006': '2006',
                'disaster prep 2007': '2007',
                'disaster prep 2008': '2008',
                'disaster prep 2009': '2009',
                'disaster prep 2010': '2010',
                'disaster prep 2011': '2011',
                'disaster prep 2012': '2012',
                'disaster prep 2013': '2013',
                'disaster prep 2014': '2014',
                'disaster prep 2015': '2015',
                'disaster prep 2016': '2016',
                'disaster prep 2017': '2017',
                'disaster prep 2018': '2018',
                'disaster prep 2019': '2019',
                'disaster prep 2020': '2020',
                'Value': 'disaster_prep_value'
                }

disaster_prep = disaster_prep.rename(columns=disaster_prep_names)
disaster_prep_panel = pd.melt(disaster_prep, id_vars=['Name', 'ISO3'], var_name='Year', value_name='disaster_prep_value')
#%% 


pop_near_sea_level = pd.read_csv('ID_INFR_04_Pop5mAboveSeaLevel.csv')
pop_near_sea_level_names = {
                'pop near sea level 1995': '1995',
                'pop near sea level 1996': '1996',
                'pop near sea level 1997': '1997',
                'pop near sea level 1998': '1998',
                'pop near sea level 1999': '1999',
                'pop near sea level 2000': '2000',
                'pop near sea level 2001': '2001',
                'pop near sea level 2002': '2002',
                'pop near sea level 2003': '2003',
                'pop near sea level 2004': '2004',
                'pop near sea level 2005': '2005',
                'pop near sea level 2006': '2006',
                'pop near sea level 2007': '2007',
                'pop near sea level 2008': '2008',
                'pop near sea level 2009': '2009',
                'pop near sea level 2010': '2010',
                'pop near sea level 2011': '2011',
                'pop near sea level 2012': '2012',
                'pop near sea level 2013': '2013',
                'pop near sea level 2014': '2014',
                'pop near sea level 2015': '2015',
                'pop near sea level 2016': '2016',
                'pop near sea level 2017': '2017',
                'pop near sea level 2018': '2018',
                'pop near sea level 2019': '2019',
                'pop near sea level 2020': '2020',
                'Value': 'pop_near_sea_level_value'
                }

pop_near_sea_level = pop_near_sea_level.rename(columns=pop_near_sea_level_names)
pop_near_sea_level_panel = pd.melt(pop_near_sea_level, id_vars=['Name', 'ISO3'], var_name='Year', value_name='pop_near_sea_level_value')

#%% 

import_energy = pd.read_csv('ID_INFR_03_ImportEnergy.csv')
import_energy_names = {
                'import energy 1995': '1995',
                'import energy 1996': '1996',
                'import energy 1997': '1997',
                'import energy 1998': '1998',
                'import energy 1999': '1999',
                'import energy 2000': '2000',
                'import energy 2001': '2001',
                'import energy 2002': '2002',
                'import energy 2003': '2003',
                'import energy 2004': '2004',
                'import energy 2005': '2005',
                'import energy 2006': '2006',
                'import energy 2007': '2007',
                'import energy 2008': '2008',
                'import energy 2009': '2009',
                'import energy 2010': '2010',
                'import energy 2011': '2011',
                'import energy 2012': '2012',
                'import energy 2013': '2013',
                'import energy 2014': '2014',
                'import energy 2015': '2015',
                'import energy 2016': '2016',
                'import energy 2017': '2017',
                'import energy 2018': '2018',
                'import energy 2019': '2019',
                'import energy 2020': '2020',
                'Value': 'import_energy_value'
                }

import_energy = import_energy.rename(columns=import_energy_names)
import_energy_panel = pd.melt(import_energy, id_vars=['Name', 'ISO3'], var_name='Year', value_name='import_energy_value')

#%% 

sanitation_facilities = pd.read_csv('ID_HEAL_06_SanitationFacilities.csv')
sanitation_facilities_names = {
                'sanitation facilities 1995': '1995',
                'sanitation facilities 1996': '1996',
                'sanitation facilities 1997': '1997',
                'sanitation facilities 1998': '1998',
                'sanitation facilities 1999': '1999',
                'sanitation facilities 2000': '2000',
                'sanitation facilities 2001': '2001',
                'sanitation facilities 2002': '2002',
                'sanitation facilities 2003': '2003',
                'sanitation facilities 2004': '2004',
                'sanitation facilities 2005': '2005',
                'sanitation facilities 2006': '2006',
                'sanitation facilities 2007': '2007',
                'sanitation facilities 2008': '2008',
                'sanitation facilities 2009': '2009',
                'sanitation facilities 2010': '2010',
                'sanitation facilities 2011': '2011',
                'sanitation facilities 2012': '2012',
                'sanitation facilities 2013': '2013',
                'sanitation facilities 2014': '2014',
                'sanitation facilities 2015': '2015',
                'sanitation facilities 2016': '2016',
                'sanitation facilities 2017': '2017',
                'sanitation facilities 2018': '2018',
                'sanitation facilities 2019': '2019',
                'sanitation facilities 2020': '2020',
                'Value': 'sanitation_facilities_value'
                }

sanitation_facilities = sanitation_facilities.rename(columns=sanitation_facilities_names)
sanitation_facilities_panel = pd.melt(sanitation_facilities, id_vars=['Name', 'ISO3'], var_name='Year', value_name='sanitation_facilities_value')

#%% 
med_staff = pd.read_csv('ID_HEAL_05_MedStaff.csv')
med_staff_names = {
                'med staff 1995': '1995',
                'med staff 1996': '1996',
                'med staff 1997': '1997',
                'med staff 1998': '1998',
                'med staff 1999': '1999',
                'med staff 2000': '2000',
                'med staff 2001': '2001',
                'med staff 2002': '2002',
                'med staff 2003': '2003',
                'med staff 2004': '2004',
                'med staff 2005': '2005',
                'med staff 2006': '2006',
                'med staff 2007': '2007',
                'med staff 2008': '2008',
                'med staff 2009': '2009',
                'med staff 2010': '2010',
                'med staff 2011': '2011',
                'med staff 2012': '2012',
                'med staff 2013': '2013',
                'med staff 2014': '2014',
                'med staff 2015': '2015',
                'med staff 2016': '2016',
                'med staff 2017': '2017',
                'med staff 2018': '2018',
                'med staff 2019': '2019',
                'med staff 2020': '2020',
                'Value': 'med_staff_value'
                }

med_staff = med_staff.rename(columns=med_staff_names)
med_staff_panel = pd.melt(med_staff, id_vars=['Name', 'ISO3'], var_name='Year', value_name='med_staff_value')

#%% 

slum = pd.read_csv('ID_HEAL_04_SLUM.csv')
slum_names = {
                'slum 1995': '1995',
                'slum 1996': '1996',
                'slum 1997': '1997',
                'slum 1998': '1998',
                'slum 1999': '1999',
                'slum 2000': '2000',
                'slum 2001': '2001',
                'slum 2002': '2002',
                'slum 2003': '2003',
                'slum 2004': '2004',
                'slum 2005': '2005',
                'slum 2006': '2006',
                'slum 2007': '2007',
                'slum 2008': '2008',
                'slum 2009': '2009',
                'slum 2010': '2010',
                'slum 2011': '2011',
                'slum 2012': '2012',
                'slum 2013': '2013',
                'slum 2014': '2014',
                'slum 2015': '2015',
                'slum 2016': '2016',
                'slum 2017': '2017',
                'slum 2018': '2018',
                'slum 2019': '2019',
                'slum 2020': '2020',
                'Value': 'slum_value'
                }

slum = slum.rename(columns=slum_names)
slum_panel = pd.melt(slum, id_vars=['Name', 'ISO3'], var_name='Year', value_name='slum_value')

#%% 

external_health_dependency = pd.read_csv('ID_HEAL_03_DepExternalHealthSvc.csv')
external_health_dependency_names = {
                'external health dependency 1995': '1995',
                'external health dependency 1996': '1996',
                'external health dependency 1997': '1997',
                'external health dependency 1998': '1998',
                'external health dependency 1999': '1999',
                'external health dependency 2000': '2000',
                'external health dependency 2001': '2001',
                'external health dependency 2002': '2002',
                'external health dependency 2003': '2003',
                'external health dependency 2004': '2004',
                'external health dependency 2005': '2005',
                'external health dependency 2006': '2006',
                'external health dependency 2007': '2007',
                'external health dependency 2008': '2008',
                'external health dependency 2009': '2009',
                'external health dependency 2010': '2010',
                'external health dependency 2011': '2011',
                'external health dependency 2012': '2012',
                'external health dependency 2013': '2013',
                'external health dependency 2014': '2014',
                'external health dependency 2015': '2015',
                'external health dependency 2016': '2016',
                'external health dependency 2017': '2017',
                'external health dependency 2018': '2018',
                'external health dependency 2019': '2019',
                'external health dependency 2020': '2020',
                'Value': 'external_health_dependency_value'
                }

external_health_dependency = external_health_dependency.rename(columns=external_health_dependency_names)
external_health_dependency_panel = pd.melt(external_health_dependency, id_vars=['Name', 'ISO3'], var_name='Year', value_name='external_health_dependency_value')

#%% 

paved_roads = pd.read_csv('ID_HABI_06_PavedRoads.csv')
paved_roads_names = {
                'paved roads 1995': '1995',
                'paved roads 1996': '1996',
                'paved roads 1997': '1997',
                'paved roads 1998': '1998',
                'paved roads 1999': '1999',
                'paved roads 2000': '2000',
                'paved roads 2001': '2001',
                'paved roads 2002': '2002',
                'paved roads 2003': '2003',
                'paved roads 2004': '2004',
                'paved roads 2005': '2005',
                'paved roads 2006': '2006',
                'paved roads 2007': '2007',
                'paved roads 2008': '2008',
                'paved roads 2009': '2009',
                'paved roads 2010': '2010',
                'paved roads 2011': '2011',
                'paved roads 2012': '2012',
                'paved roads 2013': '2013',
                'paved roads 2014': '2014',
                'paved roads 2015': '2015',
                'paved roads 2016': '2016',
                'paved roads 2017': '2017',
                'paved roads 2018': '2018',
                'paved roads 2019': '2019',
                'paved roads 2020': '2020',
                'Value': 'paved_roads_value'
                }

paved_roads = paved_roads.rename(columns=paved_roads_names)
paved_roads_panel = pd.melt(paved_roads, id_vars=['Name', 'ISO3'], var_name='Year', value_name='paved_roads_value')

#%% 

trade_transpo_quality = pd.read_csv('ID_HABI_05_TradeTranspoQuality.csv')
trade_transpo_quality_names = {
                'trade transpo quality 1995': '1995',
                'trade transpo quality 1996': '1996',
                'trade transpo quality 1997': '1997',
                'trade transpo quality 1998': '1998',
                'trade transpo quality 1999': '1999',
                'trade transpo quality 2000': '2000',
                'trade transpo quality 2001': '2001',
                'trade transpo quality 2002': '2002',
                'trade transpo quality 2003': '2003',
                'trade transpo quality 2004': '2004',
                'trade transpo quality 2005': '2005',
                'trade transpo quality 2006': '2006',
                'trade transpo quality 2007': '2007',
                'trade transpo quality 2008': '2008',
                'trade transpo quality 2009': '2009',
                'trade transpo quality 2010': '2010',
                'trade transpo quality 2011': '2011',
                'trade transpo quality 2012': '2012',
                'trade transpo quality 2013': '2013',
                'trade transpo quality 2014': '2014',
                'trade transpo quality 2015': '2015',
                'trade transpo quality 2016': '2016',
                'trade transpo quality 2017': '2017',
                'trade transpo quality 2018': '2018',
                'trade transpo quality 2019': '2019',
                'trade transpo quality 2020': '2020',
                'Value': 'trade_transpo_quality_value'
                }

trade_transpo_quality = trade_transpo_quality.rename(columns=trade_transpo_quality_names)
trade_transpo_quality_panel = pd.melt(trade_transpo_quality, id_vars=['Name', 'ISO3'], var_name='Year', value_name='trade_transpo_quality_value')

#%% 

age_dependent_ratio = pd.read_csv('ID_HABI_04_AgeDependentRatio.csv')
age_dependent_ratio_names = {
                'age dependent ratio 1995': '1995',
                'age dependent ratio 1996': '1996',
                'age dependent ratio 1997': '1997',
                'age dependent ratio 1998': '1998',
                'age dependent ratio 1999': '1999',
                'age dependent ratio 2000': '2000',
                'age dependent ratio 2001': '2001',
                'age dependent ratio 2002': '2002',
                'age dependent ratio 2003': '2003',
                'age dependent ratio 2004': '2004',
                'age dependent ratio 2005': '2005',
                'age dependent ratio 2006': '2006',
                'age dependent ratio 2007': '2007',
                'age dependent ratio 2008': '2008',
                'age dependent ratio 2009': '2009',
                'age dependent ratio 2010': '2010',
                'age dependent ratio 2011': '2011',
                'age dependent ratio 2012': '2012',
                'age dependent ratio 2013': '2013',
                'age dependent ratio 2014': '2014',
                'age dependent ratio 2015': '2015',
                'age dependent ratio 2016': '2016',
                'age dependent ratio 2017': '2017',
                'age dependent ratio 2018': '2018',
                'age dependent ratio 2019': '2019',
                'age dependent ratio 2020': '2020',
                'Value': 'age_dependent_ratio_value'
                }

age_dependent_ratio = age_dependent_ratio.rename(columns=age_dependent_ratio_names)
age_dependent_ratio_panel = pd.melt(age_dependent_ratio, id_vars=['Name', 'ISO3'], var_name='Year', value_name='age_dependent_ratio_value')

#%% 

urban_concentration = pd.read_csv('ID_HABI_03_UrbanConcentration.csv')
urban_concentration_names = {
                'urban concentration 1995': '1995',
                'urban concentration 1996': '1996',
                'urban concentration 1997': '1997',
                'urban concentration 1998': '1998',
                'urban concentration 1999': '1999',
                'urban concentration 2000': '2000',
                'urban concentration 2001': '2001',
                'urban concentration 2002': '2002',
                'urban concentration 2003': '2003',
                'urban concentration 2004': '2004',
                'urban concentration 2005': '2005',
                'urban concentration 2006': '2006',
                'urban concentration 2007': '2007',
                'urban concentration 2008': '2008',
                'urban concentration 2009': '2009',
                'urban concentration 2010': '2010',
                'urban concentration 2011': '2011',
                'urban concentration 2012': '2012',
                'urban concentration 2013': '2013',
                'urban concentration 2014': '2014',
                'urban concentration 2015': '2015',
                'urban concentration 2016': '2016',
                'urban concentration 2017': '2017',
                'urban concentration 2018': '2018',
                'urban concentration 2019': '2019',
                'urban concentration 2020': '2020',
                'Value': 'urban_concentration_value'
                }

urban_concentration = urban_concentration.rename(columns=urban_concentration_names)
urban_concentration_panel = pd.melt(urban_concentration, id_vars=['Name', 'ISO3'], var_name='Year', value_name='urban_concentration_value')

#%% 

child = pd.read_csv('ID_FOOD_06_Child.csv')
child_names = {
                'child 1995': '1995',
                'child 1996': '1996',
                'child 1997': '1997',
                'child 1998': '1998',
                'child 1999': '1999',
                'child 2000': '2000',
                'child 2001': '2001',
                'child 2002': '2002',
                'child 2003': '2003',
                'child 2004': '2004',
                'child 2005': '2005',
                'child 2006': '2006',
                'child 2007': '2007',
                'child 2008': '2008',
                'child 2009': '2009',
                'child 2010': '2010',
                'child 2011': '2011',
                'child 2012': '2012',
                'child 2013': '2013',
                'child 2014': '2014',
                'child 2015': '2015',
                'child 2016': '2016',
                'child 2017': '2017',
                'child 2018': '2018',
                'child 2019': '2019',
                'child 2020': '2020',
                'Value': 'child_value'
                }

child = child.rename(columns=child_names)
child_panel = pd.melt(child, id_vars=['Name', 'ISO3'], var_name='Year', value_name='child_value')

#%% 

ag_cap = pd.read_csv('ID_FOOD_05_AgCap.csv')
ag_cap_names = {
                'ag cap 1995': '1995',
                'ag cap 1996': '1996',
                'ag cap 1997': '1997',
                'ag cap 1998': '1998',
                'ag cap 1999': '1999',
                'ag cap 2000': '2000',
                'ag cap 2001': '2001',
                'ag cap 2002': '2002',
                'ag cap 2003': '2003',
                'ag cap 2004': '2004',
                'ag cap 2005': '2005',
                'ag cap 2006': '2006',
                'ag cap 2007': '2007',
                'ag cap 2008': '2008',
                'ag cap 2009': '2009',
                'ag cap 2010': '2010',
                'ag cap 2011': '2011',
                'ag cap 2012': '2012',
                'ag cap 2013': '2013',
                'ag cap 2014': '2014',
                'ag cap 2015': '2015',
                'ag cap 2016': '2016',
                'ag cap 2017': '2017',
                'ag cap 2018': '2018',
                'ag cap 2019': '2019',
                'ag cap 2020': '2020',
                'Value': 'ag_cap_value'
                }

ag_cap = ag_cap.rename(columns=ag_cap_names)
ag_cap_panel = pd.melt(ag_cap, id_vars=['Name', 'ISO3'], var_name='Year', value_name='ag_cap_value')

#%% 

rural_pop = pd.read_csv('ID_FOOD_04_RuralPop.csv')
rural_pop_names = {
                'rural pop 1995': '1995',
                'rural pop 1996': '1996',
                'rural pop 1997': '1997',
                'rural pop 1998': '1998',
                'rural pop 1999': '1999',
                'rural pop 2000': '2000',
                'rural pop 2001': '2001',
                'rural pop 2002': '2002',
                'rural pop 2003': '2003',
                'rural pop 2004': '2004',
                'rural pop 2005': '2005',
                'rural pop 2006': '2006',
                'rural pop 2007': '2007',
                'rural pop 2008': '2008',
                'rural pop 2009': '2009',
                'rural pop 2010': '2010',
                'rural pop 2011': '2011',
                'rural pop 2012': '2012',
                'rural pop 2013': '2013',
                'rural pop 2014': '2014',
                'rural pop 2015': '2015',
                'rural pop 2016': '2016',
                'rural pop 2017': '2017',
                'rural pop 2018': '2018',
                'rural pop 2019': '2019',
                'rural pop 2020': '2020',
                'Value': 'rural_pop_value'
                }

rural_pop = rural_pop.rename(columns=rural_pop_names)
rural_pop_panel = pd.melt(rural_pop, id_vars=['Name', 'ISO3'], var_name='Year', value_name='rural_pop_value')

#%% 

intl_enviro_con = pd.read_csv('ID_ECOS_06_IntlEnviroCon.csv')
intl_enviro_con_names = {
                'intl enviro con 1995': '1995',
                'intl enviro con 1996': '1996',
                'intl enviro con 1997': '1997',
                'intl enviro con 1998': '1998',
                'intl enviro con 1999': '1999',
                'intl enviro con 2000': '2000',
                'intl enviro con 2001': '2001',
                'intl enviro con 2002': '2002',
                'intl enviro con 2003': '2003',
                'intl enviro con 2004': '2004',
                'intl enviro con 2005': '2005',
                'intl enviro con 2006': '2006',
                'intl enviro con 2007': '2007',
                'intl enviro con 2008': '2008',
                'intl enviro con 2009': '2009',
                'intl enviro con 2010': '2010',
                'intl enviro con 2011': '2011',
                'intl enviro con 2012': '2012',
                'intl enviro con 2013': '2013',
                'intl enviro con 2014': '2014',
                'intl enviro con 2015': '2015',
                'intl enviro con 2016': '2016',
                'intl enviro con 2017': '2017',
                'intl enviro con 2018': '2018',
                'intl enviro con 2019': '2019',
                'intl enviro con 2020': '2020',
                'Value': 'intl_enviro_con_value'
                }

intl_enviro_con = intl_enviro_con.rename(columns=intl_enviro_con_names)
intl_enviro_con_panel = pd.melt(intl_enviro_con, id_vars=['Name', 'ISO3'], var_name='Year', value_name='intl_enviro_con_value')

#%%

prot_biome = pd.read_csv('ID_ECOS_05_ProtBiome.csv')
prot_biome_names = {
                'prot biome 1995': '1995',
                'prot biome 1996': '1996',
                'prot biome 1997': '1997',
                'prot biome 1998': '1998',
                'prot biome 1999': '1999',
                'prot biome 2000': '2000',
                'prot biome 2001': '2001',
                'prot biome 2002': '2002',
                'prot biome 2003': '2003',
                'prot biome 2004': '2004',
                'prot biome 2005': '2005',
                'prot biome 2006': '2006',
                'prot biome 2007': '2007',
                'prot biome 2008': '2008',
                'prot biome 2009': '2009',
                'prot biome 2010': '2010',
                'prot biome 2011': '2011',
                'prot biome 2012': '2012',
                'prot biome 2013': '2013',
                'prot biome 2014': '2014',
                'prot biome 2015': '2015',
                'prot biome 2016': '2016',
                'prot biome 2017': '2017',
                'prot biome 2018': '2018',
                'prot biome 2019': '2019',
                'prot biome 2020': '2020',
                'Value': 'prot_biome_value'
                }

prot_biome = prot_biome.rename(columns=prot_biome_names)
prot_biome_panel = pd.melt(prot_biome, id_vars=['Name', 'ISO3'], var_name='Year', value_name='prot_biome_value')

#%%  

eco_footprint = pd.read_csv('ID_ECOS_04_EcoFootprint.csv')
eco_footprint_names = {
                'eco footprint 1995': '1995',
                'eco footprint 1996': '1996',
                'eco footprint 1997': '1997',
                'eco footprint 1998': '1998',
                'eco footprint 1999': '1999',
                'eco footprint 2000': '2000',
                'eco footprint 2001': '2001',
                'eco footprint 2002': '2002',
                'eco footprint 2003': '2003',
                'eco footprint 2004': '2004',
                'eco footprint 2005': '2005',
                'eco footprint 2006': '2006',
                'eco footprint 2007': '2007',
                'eco footprint 2008': '2008',
                'eco footprint 2009': '2009',
                'eco footprint 2010': '2010',
                'eco footprint 2011': '2011',
                'eco footprint 2012': '2012',
                'eco footprint 2013': '2013',
                'eco footprint 2014': '2014',
                'eco footprint 2015': '2015',
                'eco footprint 2016': '2016',
                'eco footprint 2017': '2017',
                'eco footprint 2018': '2018',
                'eco footprint 2019': '2019',
                'eco footprint 2020': '2020',
                'Value': 'eco_footprint_value'
                }

eco_footprint = eco_footprint.rename(columns=eco_footprint_names)
eco_footprint_panel = pd.melt(eco_footprint, id_vars=['Name', 'ISO3'], var_name='Year', value_name='eco_footprint_value')

#%% 
nat_capital_dependency = pd.read_csv('ID_ECOS_03_NaturalCapDep.csv')
nat_capital_dependency_names = {
                'nat cap dependency 1995': '1995',
                'nat cap dependency 1996': '1996',
                'nat cap dependency 1997': '1997',
                'nat cap dependency 1998': '1998',
                'nat cap dependency 1999': '1999',
                'nat cap dependency 2000': '2000',
                'nat cap dependency 2001': '2001',
                'nat cap dependency 2002': '2002',
                'nat cap dependency 2003': '2003',
                'nat cap dependency 2004': '2004',
                'nat cap dependency 2005': '2005',
                'nat cap dependency 2006': '2006',
                'nat cap dependency 2007': '2007',
                'nat cap dependency 2008': '2008',
                'nat cap dependency 2009': '2009',
                'nat cap dependency 2010': '2010',
                'nat cap dependency 2011': '2011',
                'nat cap dependency 2012': '2012',
                'nat cap dependency 2013': '2013',
                'nat cap dependency 2014': '2014',
                'nat cap dependency 2015': '2015',
                'nat cap dependency 2016': '2016',
                'nat cap dependency 2017': '2017',
                'nat cap dependency 2018': '2018',
                'nat cap dependency 2019': '2019',
                'nat cap dependency 2020': '2020',
                'Value': 'nat_capital_dependency_value'
                }

nat_capital_dependency = nat_capital_dependency.rename(columns=nat_capital_dependency_names)
nat_capital_dependency_panel = pd.melt(nat_capital_dependency, id_vars=['Name', 'ISO3'], var_name='Year', value_name='nat_capital_dependency_value')



#%% 
# Converting integer panels to string data temporarily so that we can merge 
# onto name, ISO3, and year. Cannot merge object and integer data at the same
# time. 

# Merging all dataframes into merged_data dataframe. 
# Creates merged_panel_data csv. 


nat_capital_dependency_panel['Year'] = nat_capital_dependency['Year'].astype(str)
eco_footprint_panel ['Year'] = eco_footprint['Year'].astype(str)
prot_biome_panel['Year'] = prot_biome['Year'].astype(str)
intl_enviro_con_panel['Year'] = intl_enviro_con['Year'].astype(str)
rural_pop_panel ['Year'] = rural_pop['Year'].astype(str)
ag_cap_panel['Year'] = ag_cap['Year'].astype(str)
child_panel['Year'] = child['Year'].astype(str)
urban_concentration_panel['Year'] = urban_concentration['Year'].astype(str)
age_dependent_ratio_panel['Year'] = age_dependent_ratio['Year'].astype(str)
trade_transpo_quality_panel['Year'] = trade_transpo_quality['Year'].astype(str)
paved_roads_panel['Year'] = paved_roads['Year'].astype(str)
external_health_dependency_panel['Year'] = external_health_dependency['Year'].astype(str)
slum_panel['Year'] = slum['Year'].astype(str)
med_staff_panel['Year'] = med_staff['Year'].astype(str)
sanitation_facilities_panel['Year'] = sanitation_facilities['Year'].astype(str)
import_energy_panel['Year'] = import_energy['Year'].astype(str)
pop_near_sea_level_panel['Year'] = pop_near_sea_level['Year'].astype(str)
disaster_prep_panel['Year'] = disaster_prep['Year'].astype(str)
electric_access_panel['Year'] = electric_access['Year'].astype(str)
h20_withdrawal_panel['Year'] = h20_withdrawal['Year'].astype(str)
dam_cap_panel ['Year'] = dam_cap['Year'].astype(str)
reliable_water_panel['Year'] = reliable_water['Year'].astype(str)
gain_data_panel['Year'] = gain_data['Year'].astype(str)
gdp_data_panel['Year'] = gdp_data['Year'].astype(str)

#%%
merged_panel_data = pd.merge(nat_capital_dependency_panel, eco_footprint_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, prot_biome_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, intl_enviro_con_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, rural_pop_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, ag_cap_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, child_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, urban_concentration_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, age_dependent_ratio_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, trade_transpo_quality_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, paved_roads_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, external_health_dependency_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, slum_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, med_staff_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, sanitation_facilities_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, import_energy_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, pop_near_sea_level_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, disaster_prep_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, electric_access_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, h20_withdrawal_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, dam_cap_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, reliable_water_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, gain_data_panel, on=['Name', 'ISO3', 'Year'])
merged_panel_data = pd.merge(merged_panel_data, gdp_data_panel, on=['Name', 'ISO3', 'Year'])


merged_panel_data['Year'] = merged_panel_data['Year'].astype(int)
merged_panel_data = merged_panel_data.fillna(value='.')

merged_panel_data.to_csv('merged_panel_data.csv')




