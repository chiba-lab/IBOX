cd 'Data/CSV'
%%
clear all

event_table.rat =[];
event_table.date = [];
event_table.day=[];
event_table.trial_type=[];
event_table.behavior = [];
event_table.agent = [];
event_table.start_time = [];
event_table.stop_time = [];
event_table.duration = [];

filelist= dir("*.csv");

for i = 1:length(filelist)
    fstring = filelist(i).name;
    meta_data=split(fstring, "_");
    rat = string(meta_data{1});
    trialtype = string(meta_data{2});
    date = datetime(meta_data{3}, 'InputFormat', 'MMddyy');
    day = str2num(meta_data{4}(2:end));
    
    raw_table=readtable(fstring);
    
    L = length(raw_table.Var1); 
    
    event_table.rat = vertcat(event_table.rat, repmat(rat,L,1));
    event_table.date = vertcat(event_table.date, repmat(date,L,1));
    event_table.day= vertcat(event_table.day, repmat(day,L,1));
    event_table.trial_type = vertcat(event_table.trial_type, repmat(trialtype,L,1));

    if fstring == "EW3_31_021519_D21_Anno.csv"
        event_table.behavior = vertcat(event_table.behavior, raw_table.Var1);
        event_table.agent = vertcat(event_table.agent, raw_table.Var2);
        event_table.start_time = vertcat(event_table.start_time, raw_table.Var3);
        event_table.stop_time = vertcat(event_table.stop_time, raw_table.Var5);
        event_table.duration = vertcat(event_table.duration, raw_table.Var7);
    else
        event_table.behavior = vertcat(event_table.behavior, raw_table.Var1);
        event_table.agent = vertcat(event_table.agent, raw_table.Var2);
        event_table.start_time = vertcat(event_table.start_time, raw_table.Var3);
        event_table.stop_time = vertcat(event_table.stop_time, raw_table.Var4);
        event_table.duration = vertcat(event_table.duration, raw_table.Var5);
    end

end
    
    
event_table=struct2table(event_table);


save('event_table.mat', 'event_table')










