fname = file.choose()
Teams = read.csv(fname)
summary(Teams)
attach(Teams)

TB = (H + X2B + 2*X3B + 3*HR)
SLG = TB/AB
OBP = (H+BB+HBP) / (AB+BB + HBP + SF)
OPS = SLG + OBP
BRA = SLG * OBP
ADJ_OPS = OBP*1.8 + SLG
RCB = (TB*(H+BB))/(AB+BB)

#John prado`s extraordinary
XRR = (.5*(H-HR-X3B-X2B))+(.72*X2B)+(1.04*X3B)+(1.44*HR)+.33*(HBP+BB)+.18*SB-.32*CS-.098*(AB-H)
# Pete Palmer`s Linear Weights
LWTs = (.46*(H-HR-X3B-X2B))+(.8*X2B)+(1.02*X3B)+(1.4*HR)+.33*(HBP+BB)+.3*SB-.6*CS-.25*(AB-H)+701.2

Teams["RCB"] = RCB
Teams["XRR"] = XRR
Teams["LWT"] = LWTs

Teams_Runs_est = Teams[c("R", "RCB", "XRR", "LWT")]
View(Teams_Runs_est)
splom(Teams_Runs_est, xlab="Team Runs Estimators")

RvRCB = lm(R~RCB)
plot(R,RCB)
abline(RvRCB)
summary(RvRCB)$r.squared
cor(R,RCB)

RvXRR = lm(R~XRR)
plot(R,XRR)
abline(RvXRR)
summary(RvXRR)$r.squared
cor(R,XRR)

RvLWT = lm(Teams$R~Teams$LWT)
plot(Teams$R,Teams$LWT)
abline(RvLWT)
summary(RvLWT)$r.squared
cor(Teams$R,Teams$LWT)
