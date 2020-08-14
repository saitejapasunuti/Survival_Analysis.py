######################## Survival Analysis ##########################

install.packages('survminer')
#The survminer R package provides functions for facilitating survival analysis and visualization
install.packages("survival")
install.packages("ggplot2")
install.packages("Rcpp")
library(survminer)
library(survival)

patient <- read.csv(file.choose())
View(patient)

attach(patient)
str(patient)

time <- Followup
event <- Eventtype

group <- Scenario

summary(time)
summary(event)
# summary(X)
summary(group)
table(group)

# Kaplan-Meier non-parametric analysis
kmsurvival <- survfit(Surv(time,event) ~ 1)

summary(kmsurvival)

plot(kmsurvival, xlab="Time", ylab="Survival Probability")

ggsurvplot(kmsurvival, data=patient, risk.table = TRUE)


# Kaplan-Meier non-parametric analysis by group
kmsurvival1 <- survfit(Surv(time, event) ~ group)
summary(kmsurvival1)

plot(kmsurvival1, xlab="Time", ylab="Survival Probability")
ggsurvplot(kmsurvival1, data=patient, risk.table = TRUE)
