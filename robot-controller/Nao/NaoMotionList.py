from NaoMotion import NaoMotion


class NaoMotionList():
    _motions = list()

    @staticmethod
    def initialize():
        NaoMotionList._motions.append(NaoMotionList._WaveHand())
        NaoMotionList._motions.append(NaoMotionList._DisagreeGesture())
    #END initialize()

    @staticmethod
    def destroy():
        NaoMotionList._motions = list()
    #END destroy()

    @staticmethod
    def find(name):
        for motion in NaoMotionList._motions:
            if motion.name() == name:
                return motion
            #END if
        #END for
        return None
    #END find()

    @staticmethod
    def get(index):
        return NaoMotionList._motions[index]
    #END get()

    @staticmethod
    def length():
        return len(NaoMotionList._motions)
    #END length()

    @staticmethod
    def _WaveHand():
        names = list()
        times = list()
        keys = list()

        names.append("LShoulderPitch")
        times.append([ 0.72000, 1.48000, 2.16000, 2.72000, 3.40000, 4.52000])
        keys.append([ [ 1.11824, [ 3, -0.24000, 0.00000], [ 3, 0.25333, 0.00000]], [ 0.92803, [ 3, -0.25333, 0.00000], [ 3, 0.22667, 0.00000]], [ 0.94030, [ 3, -0.22667, 0.00000], [ 3, 0.18667, 0.00000]], [ 0.86207, [ 3, -0.18667, 0.00000], [ 3, 0.22667, 0.00000]], [ 0.89735, [ 3, -0.22667, 0.00000], [ 3, 0.37333, 0.00000]], [ 0.84212, [ 3, -0.37333, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("LShoulderRoll")
        times.append([ 0.72000, 1.48000, 2.16000, 2.72000, 3.40000, 4.52000])
        keys.append([ [ 0.36352, [ 3, -0.24000, 0.00000], [ 3, 0.25333, 0.00000]], [ 0.22699, [ 3, -0.25333, 0.02572], [ 3, 0.22667, -0.02301]], [ 0.20398, [ 3, -0.22667, 0.00000], [ 3, 0.18667, 0.00000]], [ 0.21779, [ 3, -0.18667, -0.00670], [ 3, 0.22667, 0.00813]], [ 0.24847, [ 3, -0.22667, 0.00000], [ 3, 0.37333, 0.00000]], [ 0.22699, [ 3, -0.37333, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("LElbowYaw")
        times.append([ 0.72000, 1.48000, 2.16000, 2.72000, 3.40000, 4.52000])
        keys.append([ [ -0.80386, [ 3, -0.24000, 0.00000], [ 3, 0.25333, 0.00000]], [ -0.69188, [ 3, -0.25333, -0.01372], [ 3, 0.22667, 0.01227]], [ -0.67960, [ 3, -0.22667, -0.01227], [ 3, 0.18667, 0.01011]], [ -0.61057, [ 3, -0.18667, 0.00000], [ 3, 0.22667, 0.00000]], [ -0.75324, [ 3, -0.22667, 0.00000], [ 3, 0.37333, 0.00000]], [ -0.67040, [ 3, -0.37333, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("LElbowRoll")
        times.append([ 0.72000, 1.48000, 2.16000, 2.72000, 3.40000, 4.52000])
        keys.append([ [ -1.37902, [ 3, -0.24000, 0.00000], [ 3, 0.25333, 0.00000]], [ -1.29005, [ 3, -0.25333, -0.03454], [ 3, 0.22667, 0.03091]], [ -1.18267, [ 3, -0.22667, 0.00000], [ 3, 0.18667, 0.00000]], [ -1.24863, [ 3, -0.18667, 0.02055], [ 3, 0.22667, -0.02496]], [ -1.31920, [ 3, -0.22667, 0.00000], [ 3, 0.37333, 0.00000]], [ -1.18421, [ 3, -0.37333, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("LWristYaw")
        times.append([ 1.48000, 4.52000])
        keys.append([ [ 0.14722, [ 3, -0.49333, 0.00000], [ 3, 1.01333, 0.00000]], [ 0.11961, [ 3, -1.01333, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("LHand")
        times.append([ 1.48000, 4.52000])
        keys.append([ [ 0.00416, [ 3, -0.49333, 0.00000], [ 3, 1.01333, 0.00000]], [ 0.00419, [ 3, -1.01333, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("RShoulderPitch")
        times.append([ 0.64000, 1.40000, 2.08000, 2.64000, 3.32000, 4.44000])
        keys.append([ [ 0.24702, [ 3, -0.21333, 0.00000], [ 3, 0.25333, 0.00000]], [ -1.17193, [ 3, -0.25333, 0.00000], [ 3, 0.22667, 0.00000]], [ -1.08910, [ 3, -0.22667, 0.00000], [ 3, 0.18667, 0.00000]], [ -1.26091, [ 3, -0.18667, 0.00000], [ 3, 0.22667, 0.00000]], [ -1.14892, [ 3, -0.22667, -0.11198], [ 3, 0.37333, 0.18444]], [ 1.02015, [ 3, -0.37333, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("RShoulderRoll")
        times.append([ 0.64000, 1.40000, 2.08000, 2.64000, 3.32000, 4.44000])
        keys.append([ [ -0.24241, [ 3, -0.21333, 0.00000], [ 3, 0.25333, 0.00000]], [ -0.95419, [ 3, -0.25333, 0.00000], [ 3, 0.22667, 0.00000]], [ -0.46024, [ 3, -0.22667, 0.00000], [ 3, 0.18667, 0.00000]], [ -0.96033, [ 3, -0.18667, 0.00000], [ 3, 0.22667, 0.00000]], [ -0.32832, [ 3, -0.22667, -0.04750], [ 3, 0.37333, 0.07823]], [ -0.25008, [ 3, -0.37333, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("RElbowYaw")
        times.append([ 0.64000, 1.40000, 2.08000, 2.64000, 3.32000, 3.72000, 4.44000])
        keys.append([ [ -0.31298, [ 3, -0.21333, 0.00000], [ 3, 0.25333, 0.00000]], [ 0.56447, [ 3, -0.25333, 0.00000], [ 3, 0.22667, 0.00000]], [ 0.39113, [ 3, -0.22667, 0.03954], [ 3, 0.18667, -0.03256]], [ 0.34818, [ 3, -0.18667, 0.00000], [ 3, 0.22667, 0.00000]], [ 0.38192, [ 3, -0.22667, -0.03375], [ 3, 0.13333, 0.01985]], [ 0.97738, [ 3, -0.13333, 0.00000], [ 3, 0.24000, 0.00000]], [ 0.82678, [ 3, -0.24000, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("RElbowRoll")
        times.append([ 0.64000, 1.40000, 1.68000, 2.08000, 2.40000, 2.64000, 3.04000, 3.32000, 3.72000, 4.44000])
        keys.append([ [ 1.38524, [ 3, -0.21333, 0.00000], [ 3, 0.25333, 0.00000]], [ 0.24241, [ 3, -0.25333, 0.00000], [ 3, 0.09333, 0.00000]], [ 0.34907, [ 3, -0.09333, -0.09496], [ 3, 0.13333, 0.13565]], [ 0.93425, [ 3, -0.13333, 0.00000], [ 3, 0.10667, 0.00000]], [ 0.68068, [ 3, -0.10667, 0.14138], [ 3, 0.08000, -0.10604]], [ 0.19199, [ 3, -0.08000, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.26180, [ 3, -0.13333, -0.06981], [ 3, 0.09333, 0.04887]], [ 0.70722, [ 3, -0.09333, -0.10397], [ 3, 0.13333, 0.14852]], [ 1.01927, [ 3, -0.13333, -0.06647], [ 3, 0.24000, 0.11965]], [ 1.26559, [ 3, -0.24000, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("RWristYaw")
        times.append([ 1.40000, 3.32000, 4.44000])
        keys.append([ [ -0.31298, [ 3, -0.46667, 0.00000], [ 3, 0.64000, 0.00000]], [ -0.30377, [ 3, -0.64000, -0.00920], [ 3, 0.37333, 0.00537]], [ 0.18250, [ 3, -0.37333, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("RHand")
        times.append([ 1.40000, 3.32000, 4.44000])
        keys.append([ [ 0.01490, [ 3, -0.46667, 0.00000], [ 3, 0.64000, 0.00000]], [ 0.01492, [ 3, -0.64000, 0.00000], [ 3, 0.37333, 0.00000]], [ 0.00742, [ 3, -0.37333, 0.00000], [ 3, 0.00000, 0.00000]]])

        motion = NaoMotion("WaveHand")
        motion.init(names, times, keys, NaoMotion.METHOD_BEZIER)
        return motion
    #END motion

    @staticmethod
    def _DisagreeGesture():
        names = list()
        times = list()
        keys = list()

        names.append("LShoulderPitch")
        times.append([ 0.50000, 0.75000, 1.00000, 1.25000, 1.50000, 1.75000, 2.00000, 2.25000, 2.45000, 2.70000, 2.95000, 3.30000, 3.55000, 3.80000, 4.05000, 4.25000, 4.50000, 4.75000, 5.00000, 5.25000])
        keys.append([ [ 0.88047, [ 3, -0.16667, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.82372, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.88047, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.75469, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.88047, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.57521, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.63810, [ 3, -0.08333, -0.02506], [ 3, 0.08333, 0.02506]], [ 0.72554, [ 3, -0.08333, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.67492, [ 3, -0.06667, 0.01954], [ 3, 0.08333, -0.02443]], [ 0.59362, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.59515, [ 3, -0.08333, -0.00064], [ 3, 0.11667, 0.00089]], [ 0.59822, [ 3, -0.11667, -0.00307], [ 3, 0.08333, 0.00219]], [ 0.77616, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.58441, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.88201, [ 3, -0.08333, -0.08465], [ 3, 0.06667, 0.06772]], [ 1.04154, [ 3, -0.06667, 0.00000], [ 3, 0.08333, 0.00000]], [ 1.04001, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 1.06762, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 1.00626, [ 3, -0.08333, 0.02020], [ 3, 0.08333, -0.02020]], [ 0.94644, [ 3, -0.08333, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("LShoulderRoll")
        times.append([ 0.25000, 0.50000, 0.75000, 1.00000, 1.25000, 1.50000, 1.75000, 2.00000, 2.25000, 2.45000, 2.70000, 2.95000, 3.30000, 3.55000, 3.80000, 4.05000, 4.25000, 4.50000, 4.75000, 5.00000])
        keys.append([ [ 0.29602, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.29755, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.29602, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.38039, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.29909, [ 3, -0.08333, 0.01227], [ 3, 0.08333, -0.01227]], [ 0.28682, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.36965, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.13802, [ 3, -0.08333, 0.04755], [ 3, 0.08333, -0.04755]], [ 0.08433, [ 3, -0.08333, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.17023, [ 3, -0.06667, -0.05022], [ 3, 0.08333, 0.06278]], [ 0.42334, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.06439, [ 3, -0.08333, 0.08309], [ 3, 0.11667, -0.11633]], [ -0.17492, [ 3, -0.11667, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.16571, [ 3, -0.08333, -0.00920], [ 3, 0.08333, 0.00920]], [ 0.17637, [ 3, -0.08333, -0.08411], [ 3, 0.08333, 0.08411]], [ 0.33897, [ 3, -0.08333, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.26381, [ 3, -0.06667, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.28068, [ 3, -0.08333, -0.00153], [ 3, 0.08333, 0.00153]], [ 0.28221, [ 3, -0.08333, -0.00153], [ 3, 0.08333, 0.00153]], [ 0.46629, [ 3, -0.08333, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("LElbowYaw")
        times.append([ 0.50000, 0.75000, 1.00000, 1.25000, 1.50000, 1.75000, 2.00000, 2.25000, 2.45000, 2.70000, 2.95000, 3.30000, 3.55000, 3.80000, 4.05000, 4.25000, 4.50000, 4.75000, 5.00000, 5.25000])
        keys.append([ [ -0.48018, [ 3, -0.16667, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.37127, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.37127, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.37127, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -1.04316, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.85295, [ 3, -0.08333, -0.05727], [ 3, 0.08333, 0.05727]], [ -0.69955, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -1.17969, [ 3, -0.08333, 0.00000], [ 3, 0.06667, 0.00000]], [ -0.91277, [ 3, -0.06667, 0.00000], [ 3, 0.08333, 0.00000]], [ -1.03396, [ 3, -0.08333, 0.05241], [ 3, 0.08333, -0.05241]], [ -1.22724, [ 3, -0.08333, 0.00000], [ 3, 0.11667, 0.00000]], [ -1.21957, [ 3, -0.11667, 0.00000], [ 3, 0.08333, 0.00000]], [ -1.23798, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -1.23184, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -1.23184, [ 3, -0.08333, 0.00000], [ 3, 0.06667, 0.00000]], [ -1.23491, [ 3, -0.06667, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.80693, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -1.12293, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.61211, [ 3, -0.08333, -0.11582], [ 3, 0.08333, 0.11582]], [ -0.42803, [ 3, -0.08333, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("LElbowRoll")
        times.append([ 0.50000, 0.75000, 1.00000, 1.25000, 1.50000, 1.75000, 2.00000, 2.25000, 2.45000, 2.70000, 2.95000, 3.30000, 3.55000, 3.80000, 4.05000, 4.25000, 4.50000, 4.75000, 5.00000, 5.25000])
        keys.append([ [ -1.29312, [ 3, -0.16667, 0.00000], [ 3, 0.08333, 0.00000]], [ -1.29312, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -1.29312, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -1.29312, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -1.29312, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -1.29619, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -1.29312, [ 3, -0.08333, -0.00307], [ 3, 0.08333, 0.00307]], [ -1.27164, [ 3, -0.08333, 0.00000], [ 3, 0.06667, 0.00000]], [ -1.29465, [ 3, -0.06667, 0.00000], [ 3, 0.08333, 0.00000]], [ -1.27931, [ 3, -0.08333, -0.00332], [ 3, 0.08333, 0.00332]], [ -1.27471, [ 3, -0.08333, 0.00000], [ 3, 0.11667, 0.00000]], [ -1.29159, [ 3, -0.11667, 0.00000], [ 3, 0.08333, 0.00000]], [ -1.28238, [ 3, -0.08333, -0.00562], [ 3, 0.08333, 0.00562]], [ -1.25784, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -1.27164, [ 3, -0.08333, 0.00000], [ 3, 0.06667, 0.00000]], [ -1.23790, [ 3, -0.06667, 0.00000], [ 3, 0.08333, 0.00000]], [ -1.27471, [ 3, -0.08333, 0.01329], [ 3, 0.08333, -0.01329]], [ -1.31766, [ 3, -0.08333, 0.00307], [ 3, 0.08333, -0.00307]], [ -1.32073, [ 3, -0.08333, 0.00307], [ 3, 0.08333, -0.00307]], [ -1.52015, [ 3, -0.08333, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("LWristYaw")
        times.append([ 0.25000, 0.75000, 1.00000, 1.25000, 1.50000, 1.75000, 2.00000, 2.25000, 2.45000, 2.70000, 2.95000, 3.30000, 3.55000, 3.80000, 4.05000, 4.25000, 4.50000, 4.75000, 5.00000, 5.25000])
        keys.append([ [ -0.09208, [ 3, -0.08333, 0.00000], [ 3, 0.16667, 0.00000]], [ 0.84979, [ 3, -0.16667, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.66571, [ 3, -0.08333, 0.15698], [ 3, 0.08333, -0.15698]], [ -0.09208, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.09208, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.02765, [ 3, -0.08333, -0.06443], [ 3, 0.08333, 0.06443]], [ 0.84826, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.84212, [ 3, -0.08333, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.84979, [ 3, -0.06667, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.84212, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.84212, [ 3, -0.08333, 0.00000], [ 3, 0.11667, 0.00000]], [ 0.75469, [ 3, -0.11667, 0.07666], [ 3, 0.08333, -0.05476]], [ 0.44789, [ 3, -0.08333, 0.06315], [ 3, 0.08333, -0.06315]], [ 0.37579, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.92956, [ 3, -0.08333, -0.02301], [ 3, 0.06667, 0.01841]], [ 0.94797, [ 3, -0.06667, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.75469, [ 3, -0.08333, 0.09511], [ 3, 0.08333, -0.09511]], [ 0.37732, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.37732, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.37732, [ 3, -0.08333, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("LHand")
        times.append([ 0.25000, 0.50000, 0.75000, 1.00000, 1.50000, 1.75000, 2.00000, 2.25000, 2.45000, 2.70000, 2.95000, 3.30000, 3.55000, 3.80000, 4.05000, 4.25000, 4.50000, 4.75000, 5.00000, 5.25000])
        keys.append([ [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.16667, 0.00000]], [ 0.01745, [ 3, -0.16667, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.01745, [ 3, -0.06667, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.11667, 0.00000]], [ 0.01745, [ 3, -0.11667, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.01745, [ 3, -0.06667, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("RShoulderPitch")
        times.append([ 0.50000, 0.75000, 1.00000, 1.25000, 1.50000, 1.75000, 2.00000, 2.25000, 2.45000, 2.70000, 2.95000, 3.30000, 3.55000, 3.80000, 4.05000, 4.25000, 4.50000, 4.75000, 5.00000, 5.25000])
        keys.append([ [ 0.91737, [ 3, -0.16667, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.61671, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.91737, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.91737, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.83761, [ 3, -0.08333, 0.07031], [ 3, 0.08333, -0.07031]], [ 0.49552, [ 3, -0.08333, 0.01074], [ 3, 0.08333, -0.01074]], [ 0.48479, [ 3, -0.08333, 0.01048], [ 3, 0.08333, -0.01048]], [ 0.43263, [ 3, -0.08333, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.54768, [ 3, -0.06667, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.40042, [ 3, -0.08333, 0.00307], [ 3, 0.08333, -0.00307]], [ 0.39735, [ 3, -0.08333, 0.00000], [ 3, 0.11667, 0.00000]], [ 0.58143, [ 3, -0.11667, -0.04743], [ 3, 0.08333, 0.03388]], [ 0.64125, [ 3, -0.08333, -0.04270], [ 3, 0.08333, 0.04270]], [ 0.83761, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.52467, [ 3, -0.08333, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.99101, [ 3, -0.06667, -0.00614], [ 3, 0.08333, 0.00767]], [ 0.99868, [ 3, -0.08333, -0.00537], [ 3, 0.08333, 0.00537]], [ 1.02322, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.99561, [ 3, -0.08333, 0.02761], [ 3, 0.08333, -0.02761]], [ 0.82533, [ 3, -0.08333, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("RShoulderRoll")
        times.append([ 0.50000, 0.75000, 1.00000, 1.25000, 1.50000, 1.75000, 2.00000, 2.25000, 2.45000, 2.70000, 2.95000, 3.30000, 3.55000, 3.80000, 4.05000, 4.25000, 4.50000, 4.75000, 5.00000, 5.25000])
        keys.append([ [ -0.34366, [ 3, -0.16667, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.25469, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.26389, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.26389, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.26389, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.25929, [ 3, -0.08333, -0.00460], [ 3, 0.08333, 0.00460]], [ -0.10742, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.37587, [ 3, -0.08333, 0.00000], [ 3, 0.06667, 0.00000]], [ -0.21940, [ 3, -0.06667, -0.06000], [ 3, 0.08333, 0.07500]], [ 0.02910, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.00456, [ 3, -0.08333, 0.02454], [ 3, 0.11667, -0.03436]], [ -0.30071, [ 3, -0.11667, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.07512, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.31758, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.08279, [ 3, -0.08333, 0.00000], [ 3, 0.06667, 0.00000]], [ -0.10282, [ 3, -0.06667, 0.04750], [ 3, 0.08333, -0.05937]], [ -0.23781, [ 3, -0.08333, 0.02889], [ 3, 0.08333, -0.02889]], [ -0.27616, [ 3, -0.08333, 0.00153], [ 3, 0.08333, -0.00153]], [ -0.27770, [ 3, -0.08333, 0.00153], [ 3, 0.08333, -0.00153]], [ -0.36974, [ 3, -0.08333, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("RElbowYaw")
        times.append([ 0.50000, 0.75000, 1.00000, 1.25000, 1.50000, 1.75000, 2.00000, 2.25000, 2.45000, 2.70000, 2.95000, 3.30000, 3.55000, 3.80000, 4.05000, 4.25000, 4.50000, 4.75000, 5.00000, 5.25000])
        keys.append([ [ 0.49697, [ 3, -0.16667, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.45862, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.45862, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.63657, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.45862, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.58134, [ 3, -0.08333, -0.06341], [ 3, 0.08333, 0.06341]], [ 0.83906, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.69486, [ 3, -0.08333, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.82218, [ 3, -0.06667, -0.03318], [ 3, 0.08333, 0.04147]], [ 0.91882, [ 3, -0.08333, -0.03835], [ 3, 0.08333, 0.03835]], [ 1.05228, [ 3, -0.08333, 0.00000], [ 3, 0.11667, 0.00000]], [ 1.04154, [ 3, -0.11667, 0.00000], [ 3, 0.08333, 0.00000]], [ 1.08910, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 1.06762, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 1.11057, [ 3, -0.08333, 0.00000], [ 3, 0.06667, 0.00000]], [ 1.02007, [ 3, -0.06667, 0.08136], [ 3, 0.08333, -0.10170]], [ 0.56140, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.82832, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.55220, [ 3, -0.08333, 0.08054], [ 3, 0.08333, -0.08054]], [ 0.34511, [ 3, -0.08333, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("RElbowRoll")
        times.append([ 0.50000, 0.75000, 1.00000, 1.25000, 1.50000, 1.75000, 2.00000, 2.25000, 2.45000, 2.70000, 2.95000, 3.30000, 3.55000, 3.80000, 4.05000, 4.25000, 4.50000, 4.75000, 5.00000, 5.25000])
        keys.append([ [ 1.29014, [ 3, -0.16667, 0.00000], [ 3, 0.08333, 0.00000]], [ 1.29014, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 1.29014, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 1.29014, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 1.24565, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 1.29474, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 1.24565, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 1.24565, [ 3, -0.08333, 0.00000], [ 3, 0.06667, 0.00000]], [ 1.24105, [ 3, -0.06667, 0.00000], [ 3, 0.08333, 0.00000]], [ 1.24258, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 1.24258, [ 3, -0.08333, 0.00000], [ 3, 0.11667, 0.00000]], [ 1.24258, [ 3, -0.11667, 0.00000], [ 3, 0.08333, 0.00000]], [ 1.24412, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 1.23798, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 1.24258, [ 3, -0.08333, -0.00460], [ 3, 0.06667, 0.00368]], [ 1.29474, [ 3, -0.06667, -0.01364], [ 3, 0.08333, 0.01704]], [ 1.33462, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 1.33155, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 1.33309, [ 3, -0.08333, -0.00102], [ 3, 0.08333, 0.00102]], [ 1.33769, [ 3, -0.08333, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("RWristYaw")
        times.append([ 0.25000, 0.50000, 0.75000, 1.00000, 1.50000, 1.75000, 2.00000, 2.25000, 2.45000, 2.70000, 2.95000, 3.30000, 3.55000, 3.80000, 4.05000, 4.25000, 4.50000, 4.75000, 5.00000, 5.25000])
        keys.append([ [ -0.04146, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.09660, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.09660, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.09660, [ 3, -0.08333, 0.00000], [ 3, 0.16667, 0.00000]], [ -0.52160, [ 3, -0.16667, 0.22021], [ 3, 0.08333, -0.11011]], [ -0.89436, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.86675, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.92044, [ 3, -0.08333, 0.00000], [ 3, 0.06667, 0.00000]], [ -0.86675, [ 3, -0.06667, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.90970, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.90970, [ 3, -0.08333, 0.00000], [ 3, 0.11667, 0.00000]], [ -0.92198, [ 3, -0.11667, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.68267, [ 3, -0.08333, -0.05292], [ 3, 0.08333, 0.05292]], [ -0.60444, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -1.22724, [ 3, -0.08333, 0.00000], [ 3, 0.06667, 0.00000]], [ -1.10912, [ 3, -0.06667, -0.09818], [ 3, 0.08333, 0.12272]], [ -0.56455, [ 3, -0.08333, -0.11914], [ 3, 0.08333, 0.11914]], [ -0.39428, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ -0.40195, [ 3, -0.08333, 0.00358], [ 3, 0.08333, -0.00358]], [ -0.41576, [ 3, -0.08333, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append("RHand")
        times.append([ 0.50000, 0.75000, 1.00000, 1.25000, 1.50000, 1.75000, 2.00000, 2.25000, 2.45000, 2.70000, 2.95000, 3.30000, 3.55000, 3.80000, 4.05000, 4.25000, 4.50000, 4.75000, 5.00000, 5.25000])
        keys.append([ [ 0.01745, [ 3, -0.16667, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.01745, [ 3, -0.06667, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.11667, 0.00000]], [ 0.01745, [ 3, -0.11667, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.01745, [ 3, -0.06667, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.08333, 0.00000]], [ 0.01745, [ 3, -0.08333, 0.00000], [ 3, 0.00000, 0.00000]]])

        motion = NaoMotion("DisagreeGesture")
        motion.init(names, times, keys, NaoMotion.METHOD_BEZIER)
        return motion
    #END motion()
#END class
