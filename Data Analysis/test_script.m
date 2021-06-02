AOPp = event_table(event_table.behavior=="AOP Nose Poke", :);
AOPa = event_table(event_table.behavior=="AOP Active Freezing", :);


AOP = [AOPp; AOPa];

AOP = sortrows(AOP, {'date', 'start_time'}); 






