redgrey_heatmap<-function(table){
	print "Remember: no clustering"
	pheatmap(table, cluster_rows=F, color = colorRampPalette(c("gray75", "darkred"))(100), cluster_cols=F, scale="none",fontsize_row=font_scale,fontsize_col=font_scale, cellwidth=font_scale, cellheight=font_scale, fontsize_number=font_scale*(2/5), border_color=NA, filename=paste("_heatmap.pdf",sep=""), display_numbers=F, drop_levels=F)
}