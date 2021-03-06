/*****************************************************************************
 * Project: RooFit                                                           *
 *                                                                           *
  * This code was autogenerated by RooClassFactory                            * 
 *****************************************************************************/

#ifndef _MGMHistRatioFunction_hh_
#define _MGMHistRatioFunction_hh_

#include "RooAbsReal.h"
#include "RooRealProxy.h"
class TH1;
class RooRealVar;
 
class MGMHistRatioFunction : public RooAbsReal {
public:
  MGMHistRatioFunction() {} ; 
  MGMHistRatioFunction(const char *name, const char *title,
	               const RooRealVar& _depVar,
	               RooAbsReal& _offsetMS,
	               RooAbsReal& _slopeMS,
	               RooAbsReal& _offsetSS,
	               RooAbsReal& _slopeSS,
	               RooAbsReal& _relative,
	               TH1&  _msHist,
	               TH1&  _ssHist);
  MGMHistRatioFunction(const MGMHistRatioFunction& other, const char* name=0) ;
  virtual TObject* clone(const char* newname) const { return new MGMHistRatioFunction(*this,newname); }
  inline virtual ~MGMHistRatioFunction() { }

protected:

  RooRealProxy fOffsetMS;
  RooRealProxy fSlopeMS;
  RooRealProxy fOffsetSS;
  RooRealProxy fSlopeSS;
  RooRealProxy fRelative;
  TH1*         fMSHist;
  TH1*         fSSHist;
  Double_t     fLowerLimit;
  Double_t     fUpperLimit;
  
  Double_t evaluate() const ;

private:

  ClassDef(MGMHistRatioFunction,1) // Your description goes here...
};
 
#endif
