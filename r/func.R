extract_evaluation <- function(tagName,colname,test_data,result_data)
{
  xgb_pred <- result_data[colname]
  test_Y <- test_data$Tag
  test_Y <- ifelse(test_Y == tagName,1,0)
  
  ROCRpred_xgb <- prediction(xgb_pred, test_Y)
  perf_xgb <- performance(ROCRpred_xgb, 'tpr','fpr')					
  roc_xgb.data <- data.frame(fpr=unlist(perf_xgb@x.values),
                             tpr=unlist(perf_xgb@y.values))
  return(roc_xgb.data)
}


get_cutoff_point <- function(perf, threshold)
{
  cutoffs <- data.frame(cut=perf@alpha.values[[1]], fpr=perf@x.values[[1]], tpr=perf@y.values[[1]])
  cutoffs <- cutoffs[order(cutoffs$tpr, decreasing=TRUE),]
  cutoffs <- subset(cutoffs, fpr <= threshold)
  if(nrow(cutoffs) == 0){ return(1.0)}
  else return(cutoffs[1, 1])
}

confusion_matrix <- function(cm, auc, color) {
  
  layout(matrix(c(1,1,2)))
  par(mar=c(0,0.1,1,0.1))
  plot(c(125, 345), c(300, 450), type = "n", xlab="", ylab="", xaxt='n', yaxt='n')
  
  # create the matrix 
  rect(150, 430, 240, 370, col=color)
  text(195, 435, '0', cex=1.2)
  rect(250, 430, 340, 370, col='white')
  text(295, 435, '1', cex=1.2)
  text(125, 370, 'Predicted', cex=1.3, srt=90, font=2)
  text(245, 450, 'Actual', cex=1.3, font=2)
  rect(150, 305, 240, 365, col='white')
  rect(250, 305, 340, 365, col=color)
  text(140, 400, '0', cex=1.2, srt=90)
  text(140, 335, '1', cex=1.2, srt=90)
  
  # add in the cm results 
  res <- as.numeric(cm$table)
  text(195, 400, res[1], cex=1.6, font=2, col='white')
  text(195, 335, res[2], cex=1.6, font=2, col='black')
  text(295, 400, res[3], cex=1.6, font=2, col='black')
  text(295, 335, res[4], cex=1.6, font=2, col='white')
  
  # add in the specifics 
  plot(c(0, 100), c(0, 50), type = "n", xlab="", ylab="", main = "", xaxt='n', yaxt='n')
  
  # add in the accuracy information 
  
  text(25, 30, "AUC", cex=1.8, font=2)
  text(25, 20, round(as.numeric(auc), 3), cex=1.8)
  text(75, 30, names(cm$overall[1]), cex=1.8, font=2)
  text(75, 20, round(as.numeric(cm$overall[1]), 3), cex=1.8)
}

draw_confusion_matrix <- function(tagName,colname,test_data,result_data,thresh,color)
{
  xgb_pred <- result_data[colname]
  test_Y <- test_data$Tag
  test_Y <- ifelse(test_Y == tagName,1,0)
  
  ROCRpred_xgb <- prediction(xgb_pred, test_Y)
  
  auc_xgb <- performance(ROCRpred_xgb, measure = "auc")
  
  perf_xgb <- performance(ROCRpred_xgb, 'tpr','fpr')
  
  cut <- get_cutoff_point(perf_xgb, thresh)
  
  pred_values_xgb <- ifelse(xgb_pred > cut,1,0)
  
  cm_xgb <- confusionMatrix(data = pred_values_xgb, reference = test_Y)
  
  confusion_matrix(cm_xgb, auc_xgb@y.values, color)
}

precision_curve <- function(tagName,colname,test_data,result_data)
{
  xgb_pred <- result_data[colname]
  test_Y <- test_data$Tag
  test_Y <- ifelse(test_Y == tagName,1,0)
  ROCRpred_xgb <- prediction(xgb_pred, test_Y)
  perf_xgb <- performance(ROCRpred_xgb,'prec', 'cutoff') #use 'prec' and 'cutoff' as measurements					
  xgb.data <- data.frame(x=unlist(perf_xgb@x.values), y=unlist(perf_xgb@y.values))
  return(xgb.data)
}

recall_curve <- function(tagName,colname,test_data,result_data)
{
  xgb_pred <- result_data[colname]
  test_Y <- test_data$Tag
  test_Y <- ifelse(test_Y == tagName,1,0)
  ROCRpred_xgb <- prediction(xgb_pred, test_Y)
  perf_xgb <- performance(ROCRpred_xgb,'rec', 'cutoff')
  xgb.data <- data.frame(x=unlist(perf_xgb@x.values), y=unlist(perf_xgb@y.values))
  return(xgb.data)
}