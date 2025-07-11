; ModuleID = "meu_programa"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare double @"read_double"()

define i32 @"main"()
{
entry:
  %"n" = alloca double
  %"i" = alloca double
  %"c" = alloca double
  %"j" = alloca double
  %"input_val" = call double @"read_double"()
  store double %"input_val", double* %"n"
  %"n_val" = load double, double* %"n"
  %"_t0" = fcmp ole double %"n_val",              0x0
  br i1 %"_t0", label %"if_true_2", label %"L0"
L0:
  store double              0x0, double* %"i"
  br label %"L2"
if_true_2:
  %".4" = bitcast [37 x i8]* @"str_const_3" to i8*
  %".5" = bitcast [3 x i8]* @"fmt_str_3" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", i8* %".4")
  %".7" = bitcast [2 x i8]* @"str_const_4" to i8*
  %".8" = bitcast [3 x i8]* @"fmt_str_4" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i8* %".7")
  br label %"L1"
L1:
  ret i32 0
L2:
  %"i_val" = load double, double* %"i"
  %"n_val.1" = load double, double* %"n"
  %"_t1" = fcmp olt double %"i_val", %"n_val.1"
  br i1 %"_t1", label %"if_true_10", label %"L3"
L3:
  br label %"L1"
if_true_10:
  store double 0x3ff0000000000000, double* %"c"
  store double              0x0, double* %"j"
  br label %"L4"
L4:
  %"j_val" = load double, double* %"j"
  %"i_val.1" = load double, double* %"i"
  %"_t2" = fcmp ole double %"j_val", %"i_val.1"
  br i1 %"_t2", label %"if_true_15", label %"L5"
L5:
  %".28" = bitcast [2 x i8]* @"str_const_30" to i8*
  %".29" = bitcast [3 x i8]* @"fmt_str_30" to i8*
  %".30" = call i32 (i8*, ...) @"printf"(i8* %".29", i8* %".28")
  %"i_val.4" = load double, double* %"i"
  %"_t9" = fadd double %"i_val.4", 0x3ff0000000000000
  store double %"_t9", double* %"i"
  br label %"L2"
if_true_15:
  %"c_val" = load double, double* %"c"
  %".18" = bitcast [3 x i8]* @"fmt_str_16" to i8*
  %".19" = call i32 (i8*, ...) @"printf"(i8* %".18", double %"c_val")
  %"j_val.1" = load double, double* %"j"
  %"i_val.2" = load double, double* %"i"
  %"_t3" = fcmp olt double %"j_val.1", %"i_val.2"
  br i1 %"_t3", label %"if_true_18", label %"L6"
L6:
  %"i_val.3" = load double, double* %"i"
  %"j_val.2" = load double, double* %"j"
  %"_t4" = fsub double %"i_val.3", %"j_val.2"
  %"c_val.1" = load double, double* %"c"
  %"_t5" = fmul double %"c_val.1", %"_t4"
  %"j_val.3" = load double, double* %"j"
  %"_t6" = fadd double %"j_val.3", 0x3ff0000000000000
  %"_t7" = fdiv double %"_t5", %"_t6"
  store double %"_t7", double* %"c"
  %"j_val.4" = load double, double* %"j"
  %"_t8" = fadd double %"j_val.4", 0x3ff0000000000000
  store double %"_t8", double* %"j"
  br label %"L4"
if_true_18:
  %".21" = bitcast [2 x i8]* @"str_const_19" to i8*
  %".22" = bitcast [3 x i8]* @"fmt_str_19" to i8*
  %".23" = call i32 (i8*, ...) @"printf"(i8* %".22", i8* %".21")
  br label %"L6"
}

@"str_const_3" = internal global [37 x i8] c"Erro: numero deve ser maior que zero\00"
@"fmt_str_3" = internal global [3 x i8] c"%s\00"
@"str_const_4" = internal global [2 x i8] c"\0a\00"
@"fmt_str_4" = internal global [3 x i8] c"%s\00"
@"fmt_str_16" = internal global [3 x i8] c"%f\00"
@"str_const_19" = internal global [2 x i8] c" \00"
@"fmt_str_19" = internal global [3 x i8] c"%s\00"
@"str_const_30" = internal global [2 x i8] c"\0a\00"
@"fmt_str_30" = internal global [3 x i8] c"%s\00"