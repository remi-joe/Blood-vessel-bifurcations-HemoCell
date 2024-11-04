% % ---------------------------------
% Remigius j Selvaraj, MSc Cranfield Univeristy
% % ---------------------------------


function [u_ratio1,u_ratio2,Ht_ratio1,Ht_ratio2,Ht_mean,Ht_std]=read_csv_2(max_iter,step_size,Diameter,Geometry,Haematocrit)
dbstop if error
    %Child vessel diameters
    if Geometry==0
        DC1=Diameter*0.93;
    end
    DC2=(Diameter^3-DC1^3)^(1/3);
    %
    dt=6.25e-8;%s
    total_record=(max_iter/step_size)+1;
    RBC_number=zeros(total_record,1);
    %Get stats from the logfile
    logfile_data=zeros(7,total_record-1);%excluding t=0
    number=0;
    line_number=0;
    first_line=55;
    path="/home/remi/irp/simulation_files/case_files/D"+num2str(Diameter,'%.1f')+"_"+num2str(Geometry)+"_"+num2str(Haematocrit)+"/output_0/log/logfile";
    fid=fopen(path);
    while ~feof(fid)
        line_number=line_number+1;
        current_line=fgetl(fid);
        if line_number>=first_line && current_line(3)=="#"
            number=number+1;
            logfile_data(1,number)=str2double(current_line...
                ((strfind(current_line,'s:')+3):(strfind(current_line,...
                '|')-2)));
            logfile_data(2,number)=str2double(current_line...
                ((strfind(current_line,'.:')+3):(strfind(current_line,...
                ', m')-5)));
            logfile_data(3,number)=str2double(current_line...
                ((strfind(current_line,'n:')+3):(strfind(current_line,...
                ', r')-5)));
            logfile_data(4,number)=str2double(current_line...
                ((strfind(current_line,'y:')+3):length(current_line)));
        end
        if line_number>=first_line && current_line(3)=="F"
            logfile_data(5,number)=str2double(...
                current_line((strfind(current_line,'n.')+4):(strfind(...
                current_line,'N,')-3)));
            logfile_data(6,number)=str2double(...
                current_line((strfind(current_line,'x.')+4):(strfind(...
                current_line,'N ')-3)));
            logfile_data(7,number)=str2double(...
                current_line((strfind(current_line,'n:')+3):(length(...
                current_line)-3)));
        end
    end
    fclose(fid);
    RBC_number(2:total_record)=logfile_data(1,:);
    %Get the number of RBCs at t=0
    file_name="/home/remi/irp/simulation_files/case_files/D"+num2str(Diameter,'%.1f')+"_"+num2str(Geometry)+"_"+num2str(Haematocrit)+"/output_0/csv/RBC."+num2str(0,'%.12d')+".csv";
    temp=csvread(file_name,1,0);
    [RBC_number(1),~]=size(temp);
    %Get stats from csv files
    dx=0.5;%um
    csv_data=zeros(RBC_number(1),7,total_record);
    %t=0
    csv_data(1:RBC_number(1),1:3,1)=temp(1:RBC_number(1),1:3)*1e6;%um
    csv_data(1:RBC_number(1),4,1)=temp(1:RBC_number(1),5)*(1e6)^3;%um3
    csv_data(1:RBC_number(1),5:7,1)=temp(1:RBC_number(1),9:11)*1e3;%mm/s
    for i=2:total_record
        file_name="/home/remi/irp/simulation_files/case_files/D"+num2str(Diameter,'%.1f')+"_"+num2str(Geometry)+"_"+num2str(Haematocrit)+"/output_0/csv/RBC."+num2str((i-1)*step_size,'%.12d')+".csv";
        temp=csvread(file_name,1,0);
        csv_data(1:RBC_number(i),1:3,i)=temp(1:RBC_number(i),1:3)*1e6;%um
        csv_data(1:RBC_number(i),4,i)=temp(1:RBC_number(i),5)*(1e6)^3;%um3
        csv_data(1:RBC_number(i),5:7,i)=temp(1:RBC_number(i),9:11)*1e3;%mm/s
    end
    %Calculate the magnitude of velocity of each RBC
    velocity=zeros(RBC_number(1),total_record);
    for i=2:total_record
        velocity(1:RBC_number(i),i)=sqrt(csv_data(1:RBC_number(i),5,i)...
            .^2+csv_data(1:RBC_number(i),6,i).^2+...
            csv_data(1:RBC_number(i),7,i).^2);
    end
    %Calculate the Ht, average velocity, line density, and flux of RBCs in 
    %each vessel
    %Vessel 5 is the combination of 1 and 4
    RBC_number_vessel=zeros(5,total_record);
    V_total=zeros(5,total_record);
    u_total=zeros(5,total_record);
    for i=1:total_record
        for j=1:RBC_number(i)
            if csv_data(j,1,i)<=5*Diameter
                %Parent vessel
                RBC_number_vessel(1,i)=RBC_number_vessel(1,i)+1;
                u_total(1,i)=u_total(1,i)+velocity(j,i);
                V_total(1,i)=V_total(1,i)+csv_data(j,4,i);
            elseif  csv_data(j,1,i)>=(1395.5-5*63.5)/63.5*Diameter
                %4th vessel
                RBC_number_vessel(4,i)=RBC_number_vessel(4,i)+1;
                u_total(4,i)=u_total(4,i)+velocity(j,i);
                V_total(4,i)=V_total(4,i)+csv_data(j,4,i);
            elseif csv_data(j,2,i)>=121.34/63.5*Diameter%
                %Upper child vessel
                RBC_number_vessel(2,i)=RBC_number_vessel(2,i)+1;
                u_total(2,i)=u_total(2,i)+velocity(j,i);
                V_total(2,i)=V_total(2,i)+csv_data(j,4,i);
            else
                %Lower child vessel
                RBC_number_vessel(3,i)=RBC_number_vessel(3,i)+1;
                u_total(3,i)=u_total(3,i)+velocity(j,i);
                V_total(3,i)=V_total(3,i)+csv_data(j,4,i);
            end
        end
    end
    RBC_number_vessel(5,:)=RBC_number_vessel(1,:)+RBC_number_vessel(4,:);
    V_total(5,:)=V_total(1,:)+V_total(4,:);
    u_total(5,:)=u_total(1,:)+u_total(4,:);
    %Ht
    V_vessel=[pi*(Diameter/2)^2*5*Diameter,pi*(DC1/2)^2*10*DC1,pi*(DC2/2)^2*10*DC1,pi*(Diameter/2)^2*5*Diameter,pi*(Diameter/2)^2*10*Diameter]';
    Ht=zeros(5,total_record);
    for i=1:total_record
        Ht(:,i)=V_total(:,i)./V_vessel*100;%pct
    end
    %average velocity
    u_mean=zeros(5,total_record);
    for i=1:total_record
        for j=1:5
            if RBC_number_vessel(j,i)~=0
                u_mean(j,i)=u_total(j,i)/RBC_number_vessel(j,i);
            end
        end
    end
    %line density
    line_density=zeros(5,total_record);
    channel_length=[5*Diameter,10*DC1,10*DC1,5*Diameter,10*Diameter]'/1000;%mm
    for i=1:total_record
        line_density(:,i)=RBC_number_vessel(:,i)./channel_length;
    end
%     %RBC flux
%     flux=u_mean.*line_density;
%     %Plot
%     t=(0:(total_record-1))*dt*10000;
%     figure
% %     plot(t,u_mean(1,:),t,u_mean(2,:),t,u_mean(3,:),t,u_mean(4,:))
%     plot(t,u_mean(1,:),t,u_mean(2,:),t,u_mean(3,:),t,u_mean(5,:))
%     xlabel('time (s)')
%     ylabel('RBC mean velocity (mm/s)')
% %     legend('parent vessel','upper child vessel','lower child vessel','4th vessel')
%     legend('parent vessel','upper child vessel','lower child vessel','combination')
%     %
%     figure
% %     plot(t,line_density(1,:),t,line_density(2,:),t,line_density(3,:),t,line_density(4,:))
%     plot(t,line_density(1,:),t,line_density(2,:),t,line_density(3,:),t,line_density(5,:))
%     xlabel('time (s)')
%     ylabel('RBC line density (RBCs/mm)')
% %     legend('parent vessel','upper child vessel','lower child vessel','4th vessel')
%     legend('parent vessel','upper child vessel','lower child vessel','combination')
%     %
%     figure
% %     plot(t,flux(1,:),t,flux(2,:),t,flux(3,:),t,flux(4,:))
%     plot(t,flux(1,:),t,flux(2,:),t,flux(3,:),t,flux(5,:))
%     xlabel('time (s)')
%     ylabel('RBC flux (RBCs/s)')
% %     legend('parent vessel','upper child vessel','lower child vessel','4th vessel')
%     legend('parent vessel','upper child vessel','lower child vessel','combination')
%     %
    Ht_global=sum(V_total(1:4,:))/sum(V_vessel(1:4,:))*100;
%     figure
%     plot(t,Ht_global)
%     xlabel('time (s)')
%     ylabel('global Ht (%)')
    %
    %Smooth the data
%     u_2=sgolayfilt(u_mean(2,:),2,3201);
%     u_3=sgolayfilt(u_mean(3,:),2,3201);
%     u_5=sgolayfilt(u_mean(5,:),2,3201);
%     H_2=sgolayfilt(Ht(2,:),2,3201);
%     H_3=sgolayfilt(Ht(3,:),2,3201);
%     H_5=sgolayfilt(Ht(5,:),2,3201);
%     u_ratio1=u_2./u_5;
%     u_ratio2=u_2./u_3;
%     Ht_ratio1=H_2./H_5;
%     Ht_ratio2=H_2./H_3;
%     Ht_mean=mean(Ht_global);
%     Ht_std=std(Ht_global);
    %
    t=(0:step_size:max_iter)*dt;
    figure(1)
    plot(t,u_mean(2,:),t,u_mean(3,:),t,u_mean(5,:),t(2:length(t)),logfile_data(3,:)*1000)
    xlabel("t (s)")
    ylabel("u_m_e_a_n (mm/s)")
    legend("larger child vessel","smaller child vessel","parent vessel","inlet fluid","location","southeast")
    title("D="+num2str(Diameter)+"um "+"H"+num2str(Haematocrit))
    figure(2)
    plot(t,u_mean(2,:)./u_mean(3,:),t,u_mean(2,:)./u_mean(5,:))
    xlabel("t (s)")
    ylabel("u_m_e_a_n ratio")
    legend("Larger child / smaller child","Larger child / parent","location","northeast")
    title("D="+num2str(Diameter)+"um "+"H"+num2str(Haematocrit))
    figure(3)
    plot(t,Ht(2,:),t,Ht(3,:),t,Ht(5,:))
    xlabel("t (s)")
    ylabel("Tube haematocrit (%)")
    legend("parent vessel","larger child vessel","smaller child vessel","location","northeast")
    title("D="+num2str(Diameter)+"um "+"H"+num2str(Haematocrit))
    figure(4)
    plot(t,Ht(2,:)./Ht(3,:),t,Ht(2,:)./Ht(5,:))
    xlabel("t (s)")
    ylabel("Tube haematocrit ratio")
    legend("Larger child / smaller child","Larger child / parent","location","northwest")
    title("D="+num2str(Diameter)+"um "+"H"+num2str(Haematocrit))
    figure(5)
    plot(t,Ht_global)
    xlabel("t (s)")
    ylabel("Total tube haematocrit (%)")
    title("D="+num2str(Diameter)+"um "+"H"+num2str(Haematocrit))
    %
    u_L_nonzero=u_mean(2,find(u_mean(2,:)~=0));
    u_S_nonzero=u_mean(3,find(u_mean(3,:)~=0));
    u_P_nonzero=u_mean(5,find(u_mean(5,:)~=0));
    u_nonzero=zeros(3,2);
    first=2;
    last=max_iter/step_size+1;
    u_nonzero(1,1)=mean(u_mean(2,first:last));
    u_nonzero(2,1)=mean(u_mean(3,first:last));
    u_nonzero(3,1)=mean(u_mean(5,first:last));
    u_nonzero(1,2)=std(u_mean(2,first:last))/mean(u_mean(2,first:last))*100;
    u_nonzero(2,2)=std(u_mean(3,first:last))/mean(u_mean(3,first:last))*100;
    u_nonzero(3,2)=std(u_mean(5,first:last))/mean(u_mean(5,first:last))*100;
%     u_nonzero(1,1)=mean(u_L_nonzero);
%     u_nonzero(2,1)=mean(u_S_nonzero);
%     u_nonzero(3,1)=mean(u_P_nonzero);
%     u_nonzero(1,2)=std(u_L_nonzero)/mean(u_L_nonzero)*100;
%     u_nonzero(2,2)=std(u_S_nonzero)/mean(u_S_nonzero)*100;
%     u_nonzero(3,2)=std(u_P_nonzero)/mean(u_P_nonzero)*100;
%     disp('u')
%     disp(u_nonzero)
%     disp(u_nonzero(1,1)/u_nonzero(2,1))
%     disp(u_nonzero(1,1)/u_nonzero(3,1))
    %
    H=zeros(3,2);
    H(1,1)=mean(Ht(2,first:last));
    H(2,1)=mean(Ht(3,first:last));
    H(3,1)=mean(Ht(5,first:last));
    H(1,2)=std(Ht(2,first:last))/mean(Ht(2,first:last))*100;
    H(2,2)=std(Ht(3,first:last))/mean(Ht(3,first:last))*100;
    H(3,2)=std(Ht(5,first:last))/mean(Ht(5,first:last))*100;
    disp('u')
    disp(u_nonzero)
    disp(u_nonzero(1,1)/u_nonzero(2,1))
    disp(u_nonzero(1,1)/u_nonzero(3,1))
    disp('Ht')
    disp(H)
    disp(H(1,1)/H(2,1))
    disp(H(1,1)/H(3,1))
    disp(max(Ht_global(first:last)))
    disp(min(Ht_global(first:last)))
    disp('maxiter')
    disp(max_iter)
    dt=6.25e-8;
    disp(max_iter*dt)
end
