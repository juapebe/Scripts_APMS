##This function is a modified version of the one made by Erik for the AP_MS pipeline

#It will produce a heat map where you only have the negatives and the bait that has been given when function was called.
#If you want to do it for all baits, just run gatherBaits - this will run the heatmap automatically.
#For input, you should use the matrix file that is produced in the APMS_pipeline > its usually called "***_wKEYS_MAT.txt"
clusterIPs = function(data_file, bait, font_scale=40){

  results_MAT = read.delim(data_file, stringsAsFactors=F)
  results_MAT = results_MAT[,results_MAT[2,]!="" & is.na(results_MAT[2,])==F]
  ## Narrow it down to the samples from same bait
  results_MAT = results_MAT[,results_MAT[2,]==bait | results_MAT[2,]=="Preys" | results_MAT[2,]=="negative"]
  results_baits = results_MAT[1,2:ncol(results_MAT)]
  results_MAT_clean = results_MAT[3:nrow(results_MAT),2:ncol(results_MAT)]
  
  colnames(results_MAT_clean) = paste(results_baits, colnames(results_baits))
  rownames(results_MAT_clean) = results_MAT[3:nrow(results_MAT),1]

  results_MAT_clean = data.matrix(results_MAT_clean)
  
  for (nc in 1:ncol(results_MAT_clean)){
  	results_MAT_clean[,nc]<-results_MAT_clean[,nc]/sum(results_MAT_clean[,nc])*100000
  }
  results_MAT_cor = cor(results_MAT_clean, use="pairwise.complete.obs", method="pearson")
  
  print(paste("Preparing heatmap for", bait))
  pheatmap(results_MAT_cor, cluster_rows=T, cluster_cols=T, scale="none",fontsize_row=font_scale,fontsize_col=font_scale, cellwidth=font_scale, cellheight=font_scale, fontsize_number=font_scale*(2/5), border_color=NA, filename=paste(bait, "_heatmap2.pdf",sep=""), display_numbers=T)

}

gatherBaits=function(file){
  results_MAT = read.delim(file, stringsAsFactors=F)
  results_MAT = results_MAT[,results_MAT[2,]!="" & is.na(results_MAT[2,])==F]
  
  all_baits=results_MAT[2,5:ncol(results_MAT)]
  all_baits=unique(as.character(all_baits))
  
  for (b in all_baits){
  	clusterIPs(file, b)
  	}
  }