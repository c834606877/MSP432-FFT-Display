################################################################################
# Automatically-generated file. Do not edit!
################################################################################

SHELL = cmd.exe

# Each subdirectory must supply rules for building sources it contributes
main.obj: ../main.c $(GEN_OPTS) | $(GEN_HDRS)
	@echo 'Building file: $<'
	@echo 'Invoking: ARM Compiler'
	"D:/ti/ccs730/ccsv7/tools/compiler/ti-cgt-arm_16.9.4.LTS/bin/armcl" -mv7M4 --code_state=16 --float_support=FPv4SPD16 -me -O2 --include_path="D:/ti/ccs730/ccsv7/ccs_base/arm/include" --include_path="D:/ti/simplelink_msp432p4_sdk_1_50_00_12/source" --include_path="D:/ti/simplelink_msp432p4_sdk_1_50_00_12/source/third_party/CMSIS/Include" --include_path="D:/ti/ccs730/ccsv7/ccs_base/arm/include/CMSIS" --include_path="C:/Users/Administrator/Documents/ccs_workspace_v7/eUART Test" --include_path="D:/ti/ccs730/ccsv7/tools/compiler/ti-cgt-arm_16.9.4.LTS/include" --advice:power="all" --define=__MSP432P401R__ --define=ARM_MATH_CM4 --define=ccs --gcc --diag_warning=225 --diag_wrap=off --display_error_number --abi=eabi --preproc_with_compile --preproc_dependency="main.d_raw" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: $<'
	@echo ' '

startup_msp432p401r_ccs.obj: ../startup_msp432p401r_ccs.c $(GEN_OPTS) | $(GEN_HDRS)
	@echo 'Building file: $<'
	@echo 'Invoking: ARM Compiler'
	"D:/ti/ccs730/ccsv7/tools/compiler/ti-cgt-arm_16.9.4.LTS/bin/armcl" -mv7M4 --code_state=16 --float_support=FPv4SPD16 -me -O2 --include_path="D:/ti/ccs730/ccsv7/ccs_base/arm/include" --include_path="D:/ti/simplelink_msp432p4_sdk_1_50_00_12/source" --include_path="D:/ti/simplelink_msp432p4_sdk_1_50_00_12/source/third_party/CMSIS/Include" --include_path="D:/ti/ccs730/ccsv7/ccs_base/arm/include/CMSIS" --include_path="C:/Users/Administrator/Documents/ccs_workspace_v7/eUART Test" --include_path="D:/ti/ccs730/ccsv7/tools/compiler/ti-cgt-arm_16.9.4.LTS/include" --advice:power="all" --define=__MSP432P401R__ --define=ARM_MATH_CM4 --define=ccs --gcc --diag_warning=225 --diag_wrap=off --display_error_number --abi=eabi --preproc_with_compile --preproc_dependency="startup_msp432p401r_ccs.d_raw" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: $<'
	@echo ' '

system_msp432p401r.obj: ../system_msp432p401r.c $(GEN_OPTS) | $(GEN_HDRS)
	@echo 'Building file: $<'
	@echo 'Invoking: ARM Compiler'
	"D:/ti/ccs730/ccsv7/tools/compiler/ti-cgt-arm_16.9.4.LTS/bin/armcl" -mv7M4 --code_state=16 --float_support=FPv4SPD16 -me -O2 --include_path="D:/ti/ccs730/ccsv7/ccs_base/arm/include" --include_path="D:/ti/simplelink_msp432p4_sdk_1_50_00_12/source" --include_path="D:/ti/simplelink_msp432p4_sdk_1_50_00_12/source/third_party/CMSIS/Include" --include_path="D:/ti/ccs730/ccsv7/ccs_base/arm/include/CMSIS" --include_path="C:/Users/Administrator/Documents/ccs_workspace_v7/eUART Test" --include_path="D:/ti/ccs730/ccsv7/tools/compiler/ti-cgt-arm_16.9.4.LTS/include" --advice:power="all" --define=__MSP432P401R__ --define=ARM_MATH_CM4 --define=ccs --gcc --diag_warning=225 --diag_wrap=off --display_error_number --abi=eabi --preproc_with_compile --preproc_dependency="system_msp432p401r.d_raw" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: $<'
	@echo ' '


