; ModuleID = "meu_programa"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"x" = alloca double
  %"y" = alloca double
  %"z" = alloca double
  store double 0x4024000000000000, double* %"x"
  %".3" = bitcast [4 x i8]* @"fmt_str_1" to i8*
  %".4" = call i32 (i8*, ...) @"scanf"(i8* %".3", double* %"y")
  %"y_val" = load double, double* %"y"
  %"_t0" = fcmp ogt double %"y_val", 0x4014000000000000
  br i1 %"_t0", label %"if_true_3", label %"L0"
L0:
  %"x_val.1" = load double, double* %"x"
  %"y_val.2" = load double, double* %"y"
  %"_t3" = fsub double %"x_val.1", %"y_val.2"
  store double %"_t3", double* %"z"
  br label %"L1"
L1:
  %"z_val" = load double, double* %"z"
  %".10" = bitcast [20 x i8]* @"fmt_str_12" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", double %"z_val")
  ret i32 0
if_true_3:
  %"x_val" = load double, double* %"x"
  %"y_val.1" = load double, double* %"y"
  %"_t1" = fmul double %"x_val", %"y_val.1"
  %"_t2" = fadd double %"_t1", 0x4000000000000000
  store double %"_t2", double* %"z"
  br label %"L1"
}

@"fmt_str_1" = constant [4 x i8] c" %lf"
@"fmt_str_12" = constant [20 x i8] c"Resultado final: %f\0a"