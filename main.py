import islpy as isl


if __name__ == "__main__":
    print(f"Currently running: {isl.isl_version()}")
    
    # Reads in a testing string of an isl map and prints it.
    isl_ctx: isl.Context = isl.Context()
    src: isl.BasicMap = isl.BasicMap.read_from_str(isl_ctx, "{ [xs, ys] -> [d0, d1] : d0=xs and d1=ys and 0 <= xs < 8 and 0 <= ys < 8 }")
    dst: isl.BasicMap = isl.BasicMap.read_from_str(isl_ctx, "{ [xd, yd] -> [d0, d1] : d0=xd and 0 <= d1 < 8 and 0 <= xd < 8 and 0 <= yd < 8 }")